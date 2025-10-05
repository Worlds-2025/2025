import argparse
import json
import math
import random
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

GAMMA = 0.5
NOISE_MIN = 0.8
NOISE_MAX = 1.2

TEAM_METADATA: Dict[str, Dict[str, str]] = {
    "Gen.G": {"region": "LCK"},
    "Hanwha Life Esports": {"region": "LCK"},
    "Bilibili Gaming": {"region": "LPL"},
    "T1": {"region": "LCK"},
    "Anyone's Legend": {"region": "LPL"},
    "Top Esports": {"region": "LPL"},
    "KT Rolster": {"region": "LCK"},
    "Invictus Gaming": {"region": "LPL"},
    "G2 Esports": {"region": "LEC"},
    "FlyQuest": {"region": "LCS"},
    "Movistar KOI": {"region": "LEC"},
    "CTBC Flying Oyster": {"region": "PCS"},
    "PSG Talon": {"region": "PCS"},
    "Fnatic": {"region": "LEC"},
    "100 Thieves": {"region": "LCS"},
    "Team Secret Whales": {"region": "PCS"},
    "Vivo Keyd Stars": {"region": "CBLOL"},
}

POOL1_BASE = [
    "Bilibili Gaming",
    "Gen.G",
    "CTBC Flying Oyster",
    "G2 Esports",
    "FlyQuest",
]

POOL2_BASE = [
    "Anyone's Legend",
    "Hanwha Life Esports",
    "Team Secret Whales",
    "Movistar KOI",
    "Vivo Keyd Stars",
]

POOL3_BASE = [
    "PSG Talon",
    "Fnatic",
    "100 Thieves",
]

PLAY_IN_SERIES = [
    ("KT Rolster", "Top Esports", "Pool 2 seeding"),
    ("Invictus Gaming", "T1", "Swiss berth decider"),
]

@dataclass
class SeriesResult:
    stage: str
    round_label: str
    team_a: str
    team_b: str
    best_of: int
    base_game_prob: float
    game_multipliers: List[float]
    per_game_probs: List[float]
    game_winners: List[str]
    winner: str
    score: Tuple[int, int]
    series_win_prob: float


def logistic(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def series_probability(p: float, best_of: int) -> float:
    needed = best_of // 2 + 1
    total = 0.0
    for k in range(needed, best_of + 1):
        combinations = math.comb(best_of, k)
        total += combinations * (p ** k) * ((1 - p) ** (best_of - k))
    return total


def simulate_series(team_a: str, team_b: str, strengths: Dict[str, float], rng: random.Random, best_of: int, stage: str, round_label: str) -> SeriesResult:
    wins_needed = best_of // 2 + 1
    score_a = 0
    score_b = 0
    game_multipliers: List[float] = []
    per_game_probs: List[float] = []
    game_winners: List[str] = []
    base_game_prob = logistic(GAMMA * (strengths[team_a] - strengths[team_b]))
    while score_a < wins_needed and score_b < wins_needed:
        multiplier = rng.uniform(NOISE_MIN, NOISE_MAX)
        adjusted = max(min(base_game_prob * multiplier, 0.99), 0.01)
        if rng.random() < adjusted:
            score_a += 1
            game_winners.append(team_a)
        else:
            score_b += 1
            game_winners.append(team_b)
        game_multipliers.append(multiplier)
        per_game_probs.append(adjusted)
    winner = team_a if score_a > score_b else team_b
    series_win_prob = base_game_prob if best_of == 1 else series_probability(base_game_prob, best_of)
    return SeriesResult(
        stage=stage,
        round_label=round_label,
        team_a=team_a,
        team_b=team_b,
        best_of=best_of,
        base_game_prob=base_game_prob,
        game_multipliers=game_multipliers,
        per_game_probs=per_game_probs,
        game_winners=game_winners,
        winner=winner,
        score=(score_a, score_b),
        series_win_prob=series_win_prob,
    )


def load_odds(path: Path) -> Dict[str, Dict[str, float]]:
    return json.loads(path.read_text())


def sample_odds(ranges: Dict[str, Dict[str, float]], rng: random.Random) -> Dict[str, float]:
    sampled = {}
    for team, bounds in ranges.items():
        sampled[team] = rng.uniform(bounds["min"], bounds["max"])
    return sampled


def normalize_probabilities(odds: Dict[str, float]) -> Tuple[Dict[str, float], Dict[str, float]]:
    raw_prob = {team: 1.0 / value for team, value in odds.items()}
    total = sum(raw_prob.values())
    normalized = {team: value / total for team, value in raw_prob.items()}
    fair_odds = {team: 1.0 / prob for team, prob in normalized.items()}
    return normalized, fair_odds


def compute_strengths(probabilities: Dict[str, float]) -> Dict[str, float]:
    return {team: math.log(prob) for team, prob in probabilities.items()}


def format_score(score: Tuple[int, int], team_a: str) -> str:
    return f"{score[0]}-{score[1]}" if score[0] >= score[1] else f"{score[1]}-{score[0]}"


def simulate_play_ins(strengths: Dict[str, float], rng: random.Random) -> Tuple[List[SeriesResult], Dict[str, str], str]:
    results: List[SeriesResult] = []
    pool2_seed = None
    pool3_seed = None
    swiss_berth = None
    eliminated = None
    # First series decides KT/TES placement
    kt_series = simulate_series("KT Rolster", "Top Esports", strengths, rng, 5, "Play-In", "KT vs TES seeding")
    results.append(kt_series)
    if kt_series.winner == "KT Rolster":
        pool2_seed = "KT Rolster"
        pool3_seed = "Top Esports"
    else:
        pool2_seed = "Top Esports"
        pool3_seed = "KT Rolster"
    # Second series decides IG vs T1 berth
    ig_series = simulate_series("Invictus Gaming", "T1", strengths, rng, 5, "Play-In", "IG vs T1 qualification")
    results.append(ig_series)
    swiss_berth = ig_series.winner
    eliminated = "T1" if swiss_berth == "Invictus Gaming" else "Invictus Gaming"
    seeds = {
        "pool2": pool2_seed,
        "pool3_from_pool2_pair": pool3_seed,
        "pool3_play_in": swiss_berth,
    }
    return results, seeds, eliminated


def avoid_same_region_pairing(pool1: List[str], pool3: List[str], rng: random.Random) -> List[Tuple[str, str]]:
    attempts = 0
    while attempts < 1000:
        shuffled = pool3[:]
        rng.shuffle(shuffled)
        pairs = list(zip(pool1, shuffled))
        if all(TEAM_METADATA[a]["region"] != TEAM_METADATA[b]["region"] for a, b in pairs):
            return pairs
        attempts += 1
    return pairs


def pair_within_group(group: List[str], rng: random.Random, disallowed: set) -> List[Tuple[str, str]]:
    attempts = 0
    while attempts < 1000:
        shuffled = group[:]
        rng.shuffle(shuffled)
        pairs = [(shuffled[i], shuffled[i + 1]) for i in range(0, len(shuffled), 2)]
        if all(frozenset(pair) not in disallowed for pair in pairs):
            return pairs
        attempts += 1
    return pairs


def simulate_swiss(strengths: Dict[str, float], seeds: Dict[str, str], rng: random.Random) -> Tuple[List[SeriesResult], Dict[str, Tuple[int, int]]]:
    swiss_results: List[SeriesResult] = []
    disallowed = set()

    pool1 = POOL1_BASE[:]
    pool2 = POOL2_BASE[:] + [seeds["pool2"]]
    pool3 = POOL3_BASE[:] + [seeds["pool3_from_pool2_pair"], seeds["pool3_play_in"]]

    participants = pool1 + pool2 + pool3
    records: Dict[str, List[int]] = {team: [0, 0] for team in participants}

    # Round 1 pairings
    pool1_pairs = avoid_same_region_pairing(pool1, pool3, rng)
    pool2_pairs = pair_within_group(pool2, rng, disallowed)

    for team_a, team_b in pool1_pairs + pool2_pairs:
        result = simulate_series(team_a, team_b, strengths, rng, 1, "Swiss", "Round 1")
        swiss_results.append(result)
        winner = result.winner
        loser = team_a if winner == team_b else team_b
        records[winner][0] += 1
        records[loser][1] += 1
        disallowed.add(frozenset((team_a, team_b)))

    # Subsequent rounds
    for round_number in range(2, 6):
        round_label = f"Round {round_number}"
        groups = defaultdict(list)
        for team, (wins, losses) in records.items():
            if wins == 3 or losses == 3:
                continue
            groups[(wins, losses)].append(team)
        for (wins, losses), group in sorted(groups.items(), key=lambda item: (-item[0][0], item[0][1])):
            if len(group) % 2 != 0:
                continue
            best_of = 3 if wins == 2 or losses == 2 else 1
            pairs = pair_within_group(group, rng, disallowed)
            for team_a, team_b in pairs:
                result = simulate_series(team_a, team_b, strengths, rng, best_of, "Swiss", round_label)
                swiss_results.append(result)
                winner = result.winner
                loser = team_a if winner == team_b else team_b
                records[winner][0] += 1
                records[loser][1] += 1
                disallowed.add(frozenset((team_a, team_b)))
    final_records = {team: tuple(record) for team, record in records.items()}
    return swiss_results, final_records


def seed_knockouts(records: Dict[str, Tuple[int, int]], swiss_results: List[SeriesResult], rng: random.Random) -> List[Tuple[str, str]]:
    advanced = [team for team, (wins, losses) in records.items() if wins == 3]
    three_zero = [team for team in advanced if records[team] == (3, 0)]
    three_one = [team for team in advanced if records[team] == (3, 1)]
    three_two = [team for team in advanced if records[team] == (3, 2)]

    rng.shuffle(three_zero)
    rng.shuffle(three_one)
    rng.shuffle(three_two)

    bracket = []
    assigned_three_two = []
    for team in three_zero:
        if three_two:
            opponent = three_two.pop()
        else:
            opponent = three_one.pop()
        assigned_three_two.append(opponent)
        bracket.append((team, opponent))
    remaining = three_one + three_two
    rng.shuffle(remaining)
    for i in range(0, len(remaining), 2):
        bracket.append((remaining[i], remaining[i + 1]))
    return bracket


def simulate_knockouts(bracket: List[Tuple[str, str]], strengths: Dict[str, float], rng: random.Random) -> Tuple[List[SeriesResult], Dict[str, str]]:
    results: List[SeriesResult] = []
    semifinalists = []
    for idx, (team_a, team_b) in enumerate(bracket, start=1):
        result = simulate_series(team_a, team_b, strengths, rng, 5, "Knockout", f"Quarterfinal {idx}")
        results.append(result)
        semifinalists.append(result.winner)
    rng.shuffle(semifinalists)
    finalists = []
    for idx in range(0, len(semifinalists), 2):
        team_a = semifinalists[idx]
        team_b = semifinalists[idx + 1]
        result = simulate_series(team_a, team_b, strengths, rng, 5, "Knockout", f"Semifinal {idx // 2 + 1}")
        results.append(result)
        finalists.append(result.winner)
    final_match = simulate_series(finalists[0], finalists[1], strengths, rng, 5, "Knockout", "Grand Final")
    results.append(final_match)
    placements = {
        "Champion": final_match.winner,
        "Runner-up": finalists[0] if final_match.winner == finalists[1] else finalists[1],
    }
    return results, placements


def render_series(result: SeriesResult, include_games: bool = True) -> str:
    score = f"{result.score[0]}-{result.score[1]}" if result.winner == result.team_a else f"{result.score[1]}-{result.score[0]}"
    header = f"- {result.team_a} vs {result.team_b} ({result.stage} {result.round_label}, Bo{result.best_of}): {result.winner} {score}"
    detail_lines = [
        f"  - Base single-game win probability for {result.team_a}: {result.base_game_prob:.3f} (series win probability {result.series_win_prob:.3f})"
    ]
    if include_games:
        for idx, (mult, prob, winner) in enumerate(zip(result.game_multipliers, result.per_game_probs, result.game_winners), start=1):
            detail_lines.append(
                f"  - Game {idx}: multiplier {mult:.3f}, adjusted P({result.team_a}) = {prob:.3f}, winner = {winner}"
            )
    return "\n".join([header] + detail_lines)


def build_markdown(
    seed: int,
    sampled_odds: Dict[str, float],
    probabilities: Dict[str, float],
    fair_odds: Dict[str, float],
    strengths: Dict[str, float],
    play_in_results: List[SeriesResult],
    seeds: Dict[str, str],
    play_in_eliminated: str,
    swiss_results: List[SeriesResult],
    records: Dict[str, Tuple[int, int]],
    bracket: List[Tuple[str, str]],
    knockout_results: List[SeriesResult],
    placements: Dict[str, str],
) -> str:
    lines: List[str] = []
    lines.append("# 2025 Worlds Simulation")
    lines.append("")
    lines.append(f"- Random seed: `{seed}`")
    lines.append("- Noise multiplier per game sampled uniformly from [0.8, 1.2]")
    lines.append("")
    lines.append("## Champion Odds Sampling")
    lines.append("")
    lines.append("| Team | Sampled Champion Odds | Normalized Title Probability | Fair Odds (no vig) | Strength s = ln(p) |")
    lines.append("| --- | --- | --- | --- | --- |")
    for team in sorted(sampled_odds, key=lambda t: probabilities[t], reverse=True):
        lines.append(
            f"| {team} | {sampled_odds[team]:.2f} | {probabilities[team]:.4f} | {fair_odds[team]:.2f} | {strengths[team]:.4f} |"
        )
    lines.append("")
    lines.append("## Play-In Stage")
    lines.append("")
    for result in play_in_results:
        lines.append(render_series(result))
        lines.append("")
    lines.append(f"- Pool 2 slot: {seeds['pool2']}")
    lines.append(f"- Pool 3 slot (from KT/TES series): {seeds['pool3_from_pool2_pair']}")
    lines.append(f"- Final Swiss qualifier: {seeds['pool3_play_in']}")
    lines.append(f"- Play-in eliminated team: {play_in_eliminated}")
    lines.append("")
    lines.append("## Swiss Stage")
    lines.append("")
    for result in swiss_results:
        lines.append(render_series(result))
        lines.append("")
    lines.append("### Swiss Records")
    lines.append("")
    lines.append("| Team | Record | Outcome |")
    lines.append("| --- | --- | --- |")
    for team, (wins, losses) in sorted(records.items(), key=lambda item: (-item[1][0], item[1][1], item[0])):
        if wins == 3:
            outcome = "Advanced"
        elif losses == 3:
            outcome = "Eliminated"
        else:
            outcome = "Incomplete"
        lines.append(f"| {team} | {wins}-{losses} | {outcome} |")
    lines.append("")
    lines.append("## Knockout Stage")
    lines.append("")
    lines.append("### Quarterfinal Draw")
    lines.append("")
    for a, b in bracket:
        lines.append(f"- {a} vs {b}")
    lines.append("")
    for result in knockout_results:
        lines.append(render_series(result))
        lines.append("")
    lines.append("### Podium")
    lines.append("")
    for key, value in placements.items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate the 2025 Worlds bracket")
    parser.add_argument("--seed", type=int, default=None, help="Random seed")
    parser.add_argument("--odds", type=Path, default=Path("data/odds_ranges.json"), help="Path to odds range JSON")
    parser.add_argument("--output", type=Path, default=Path("reports/worlds2025_simulation.md"), help="Output markdown path")
    args = parser.parse_args()

    seed = args.seed if args.seed is not None else random.randrange(1, 1_000_000_000)
    rng = random.Random(seed)

    odds_ranges = load_odds(args.odds)
    sampled_odds = sample_odds(odds_ranges, rng)
    probabilities, fair_odds = normalize_probabilities(sampled_odds)
    strengths = compute_strengths(probabilities)

    play_in_results, seeds, eliminated = simulate_play_ins(strengths, rng)
    seeds["eliminated"] = eliminated

    swiss_results, records = simulate_swiss(strengths, seeds, rng)

    bracket = seed_knockouts(records, swiss_results, rng)
    knockout_results, placements = simulate_knockouts(bracket, strengths, rng)

    markdown = build_markdown(
        seed,
        sampled_odds,
        probabilities,
        fair_odds,
        strengths,
        play_in_results,
        seeds,
        eliminated,
        swiss_results,
        records,
        bracket,
        knockout_results,
        placements,
    )
    args.output.write_text(markdown)
    print(f"Simulation complete with seed {seed}. Report written to {args.output}")


if __name__ == "__main__":
    main()
