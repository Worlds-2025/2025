# 2025 Worlds Simulation

- Random seed: `20250113`
- Noise multiplier per game sampled uniformly from [0.8, 1.2]

## Champion Odds Sampling

| Team | Sampled Champion Odds | Normalized Title Probability | Fair Odds (no vig) | Strength s = ln(p) |
| --- | --- | --- | --- | --- |
| Gen.G | 2.23 | 0.2799 | 3.57 | -1.2733 |
| Hanwha Life Esports | 3.13 | 0.1992 | 5.02 | -1.6136 |
| Bilibili Gaming | 5.17 | 0.1206 | 8.29 | -2.1154 |
| T1 | 6.29 | 0.0993 | 10.07 | -2.3099 |
| Top Esports | 6.58 | 0.0949 | 10.54 | -2.3551 |
| Anyone's Legend | 9.43 | 0.0662 | 15.11 | -2.7154 |
| KT Rolster | 20.72 | 0.0301 | 33.21 | -3.5029 |
| Invictus Gaming | 22.45 | 0.0278 | 35.98 | -3.5829 |
| G2 Esports | 42.22 | 0.0148 | 67.68 | -4.2147 |
| Movistar KOI | 54.64 | 0.0114 | 87.58 | -4.4725 |
| PSG Talon | 54.72 | 0.0114 | 87.70 | -4.4739 |
| FlyQuest | 57.40 | 0.0109 | 92.00 | -4.5218 |
| CTBC Flying Oyster | 71.81 | 0.0087 | 115.09 | -4.7457 |
| Team Secret Whales | 77.89 | 0.0080 | 124.85 | -4.8271 |
| Fnatic | 79.07 | 0.0079 | 126.73 | -4.8420 |
| 100 Thieves | 117.82 | 0.0053 | 188.84 | -5.2409 |
| Vivo Keyd Stars | 165.75 | 0.0038 | 265.65 | -5.5822 |

## Play-In Stage

- KT Rolster vs Top Esports (Play-In KT vs TES seeding, Bo5): KT Rolster 3-1
  - Base single-game win probability for KT Rolster: 0.360 (series win probability 0.251)
  - Game 1: multiplier 1.161, adjusted P(KT Rolster) = 0.418, winner = KT Rolster
  - Game 2: multiplier 0.883, adjusted P(KT Rolster) = 0.318, winner = Top Esports
  - Game 3: multiplier 1.133, adjusted P(KT Rolster) = 0.408, winner = KT Rolster
  - Game 4: multiplier 0.821, adjusted P(KT Rolster) = 0.296, winner = KT Rolster

- Invictus Gaming vs T1 (Play-In IG vs T1 qualification, Bo5): Invictus Gaming 3-1
  - Base single-game win probability for Invictus Gaming: 0.346 (series win probability 0.229)
  - Game 1: multiplier 0.858, adjusted P(Invictus Gaming) = 0.297, winner = T1
  - Game 2: multiplier 0.961, adjusted P(Invictus Gaming) = 0.332, winner = Invictus Gaming
  - Game 3: multiplier 1.167, adjusted P(Invictus Gaming) = 0.404, winner = Invictus Gaming
  - Game 4: multiplier 1.174, adjusted P(Invictus Gaming) = 0.406, winner = Invictus Gaming

- Pool 2 slot: KT Rolster
- Pool 3 slot (from KT/TES series): Top Esports
- Final Swiss qualifier: Invictus Gaming
- Play-in eliminated team: T1

## Swiss Stage

- Bilibili Gaming vs Fnatic (Swiss Round 1, Bo1): Bilibili Gaming 1-0
  - Base single-game win probability for Bilibili Gaming: 0.796 (series win probability 0.796)
  - Game 1: multiplier 0.996, adjusted P(Bilibili Gaming) = 0.793, winner = Bilibili Gaming

- Gen.G vs Invictus Gaming (Swiss Round 1, Bo1): Gen.G 1-0
  - Base single-game win probability for Gen.G: 0.760 (series win probability 0.760)
  - Game 1: multiplier 0.840, adjusted P(Gen.G) = 0.638, winner = Gen.G

- CTBC Flying Oyster vs 100 Thieves (Swiss Round 1, Bo1): CTBC Flying Oyster 1-0
  - Base single-game win probability for CTBC Flying Oyster: 0.562 (series win probability 0.562)
  - Game 1: multiplier 1.170, adjusted P(CTBC Flying Oyster) = 0.657, winner = CTBC Flying Oyster

- G2 Esports vs PSG Talon (Swiss Round 1, Bo1): G2 Esports 1-0
  - Base single-game win probability for G2 Esports: 0.532 (series win probability 0.532)
  - Game 1: multiplier 1.067, adjusted P(G2 Esports) = 0.568, winner = G2 Esports

- FlyQuest vs Top Esports (Swiss Round 1, Bo1): Top Esports 1-0
  - Base single-game win probability for FlyQuest: 0.253 (series win probability 0.253)
  - Game 1: multiplier 1.159, adjusted P(FlyQuest) = 0.293, winner = Top Esports

- Hanwha Life Esports vs Movistar KOI (Swiss Round 1, Bo1): Movistar KOI 1-0
  - Base single-game win probability for Hanwha Life Esports: 0.807 (series win probability 0.807)
  - Game 1: multiplier 1.006, adjusted P(Hanwha Life Esports) = 0.812, winner = Movistar KOI

- Vivo Keyd Stars vs Anyone's Legend (Swiss Round 1, Bo1): Anyone's Legend 1-0
  - Base single-game win probability for Vivo Keyd Stars: 0.193 (series win probability 0.193)
  - Game 1: multiplier 1.172, adjusted P(Vivo Keyd Stars) = 0.226, winner = Anyone's Legend

- Team Secret Whales vs KT Rolster (Swiss Round 1, Bo1): Team Secret Whales 1-0
  - Base single-game win probability for Team Secret Whales: 0.340 (series win probability 0.340)
  - Game 1: multiplier 0.855, adjusted P(Team Secret Whales) = 0.291, winner = Team Secret Whales

- Gen.G vs Top Esports (Swiss Round 2, Bo1): Top Esports 1-0
  - Base single-game win probability for Gen.G: 0.632 (series win probability 0.632)
  - Game 1: multiplier 1.105, adjusted P(Gen.G) = 0.698, winner = Top Esports

- Anyone's Legend vs CTBC Flying Oyster (Swiss Round 2, Bo1): Anyone's Legend 1-0
  - Base single-game win probability for Anyone's Legend: 0.734 (series win probability 0.734)
  - Game 1: multiplier 0.950, adjusted P(Anyone's Legend) = 0.697, winner = Anyone's Legend

- Bilibili Gaming vs Movistar KOI (Swiss Round 2, Bo1): Movistar KOI 1-0
  - Base single-game win probability for Bilibili Gaming: 0.765 (series win probability 0.765)
  - Game 1: multiplier 1.187, adjusted P(Bilibili Gaming) = 0.908, winner = Movistar KOI

- Team Secret Whales vs G2 Esports (Swiss Round 2, Bo1): Team Secret Whales 1-0
  - Base single-game win probability for Team Secret Whales: 0.424 (series win probability 0.424)
  - Game 1: multiplier 0.919, adjusted P(Team Secret Whales) = 0.390, winner = Team Secret Whales

- Hanwha Life Esports vs Invictus Gaming (Swiss Round 2, Bo1): Hanwha Life Esports 1-0
  - Base single-game win probability for Hanwha Life Esports: 0.728 (series win probability 0.728)
  - Game 1: multiplier 0.949, adjusted P(Hanwha Life Esports) = 0.691, winner = Hanwha Life Esports

- 100 Thieves vs PSG Talon (Swiss Round 2, Bo1): 100 Thieves 1-0
  - Base single-game win probability for 100 Thieves: 0.405 (series win probability 0.405)
  - Game 1: multiplier 0.914, adjusted P(100 Thieves) = 0.371, winner = 100 Thieves

- FlyQuest vs KT Rolster (Swiss Round 2, Bo1): FlyQuest 1-0
  - Base single-game win probability for FlyQuest: 0.375 (series win probability 0.375)
  - Game 1: multiplier 0.995, adjusted P(FlyQuest) = 0.374, winner = FlyQuest

- Vivo Keyd Stars vs Fnatic (Swiss Round 2, Bo1): Fnatic 1-0
  - Base single-game win probability for Vivo Keyd Stars: 0.409 (series win probability 0.409)
  - Game 1: multiplier 1.130, adjusted P(Vivo Keyd Stars) = 0.462, winner = Fnatic

- Top Esports vs Team Secret Whales (Swiss Round 3, Bo3): Top Esports 2-0
  - Base single-game win probability for Top Esports: 0.775 (series win probability 0.871)
  - Game 1: multiplier 1.034, adjusted P(Top Esports) = 0.801, winner = Top Esports
  - Game 2: multiplier 1.022, adjusted P(Top Esports) = 0.792, winner = Top Esports

- Movistar KOI vs Anyone's Legend (Swiss Round 3, Bo3): Anyone's Legend 2-0
  - Base single-game win probability for Movistar KOI: 0.293 (series win probability 0.208)
  - Game 1: multiplier 0.913, adjusted P(Movistar KOI) = 0.268, winner = Anyone's Legend
  - Game 2: multiplier 0.885, adjusted P(Movistar KOI) = 0.260, winner = Anyone's Legend

- Bilibili Gaming vs Gen.G (Swiss Round 3, Bo1): Gen.G 1-0
  - Base single-game win probability for Bilibili Gaming: 0.396 (series win probability 0.396)
  - Game 1: multiplier 1.145, adjusted P(Bilibili Gaming) = 0.454, winner = Gen.G

- 100 Thieves vs Fnatic (Swiss Round 3, Bo1): 100 Thieves 1-0
  - Base single-game win probability for 100 Thieves: 0.450 (series win probability 0.450)
  - Game 1: multiplier 1.103, adjusted P(100 Thieves) = 0.497, winner = 100 Thieves

- FlyQuest vs CTBC Flying Oyster (Swiss Round 3, Bo1): CTBC Flying Oyster 1-0
  - Base single-game win probability for FlyQuest: 0.528 (series win probability 0.528)
  - Game 1: multiplier 0.801, adjusted P(FlyQuest) = 0.423, winner = CTBC Flying Oyster

- Hanwha Life Esports vs G2 Esports (Swiss Round 3, Bo1): Hanwha Life Esports 1-0
  - Base single-game win probability for Hanwha Life Esports: 0.786 (series win probability 0.786)
  - Game 1: multiplier 1.015, adjusted P(Hanwha Life Esports) = 0.798, winner = Hanwha Life Esports

- KT Rolster vs PSG Talon (Swiss Round 3, Bo3): PSG Talon 2-0
  - Base single-game win probability for KT Rolster: 0.619 (series win probability 0.675)
  - Game 1: multiplier 0.811, adjusted P(KT Rolster) = 0.502, winner = PSG Talon
  - Game 2: multiplier 0.970, adjusted P(KT Rolster) = 0.600, winner = PSG Talon

- Vivo Keyd Stars vs Invictus Gaming (Swiss Round 3, Bo3): Invictus Gaming 2-0
  - Base single-game win probability for Vivo Keyd Stars: 0.269 (series win probability 0.178)
  - Game 1: multiplier 0.973, adjusted P(Vivo Keyd Stars) = 0.262, winner = Invictus Gaming
  - Game 2: multiplier 1.182, adjusted P(Vivo Keyd Stars) = 0.318, winner = Invictus Gaming

- Hanwha Life Esports vs Gen.G (Swiss Round 4, Bo3): Gen.G 2-1
  - Base single-game win probability for Hanwha Life Esports: 0.458 (series win probability 0.437)
  - Game 1: multiplier 1.185, adjusted P(Hanwha Life Esports) = 0.542, winner = Gen.G
  - Game 2: multiplier 1.126, adjusted P(Hanwha Life Esports) = 0.515, winner = Hanwha Life Esports
  - Game 3: multiplier 0.803, adjusted P(Hanwha Life Esports) = 0.368, winner = Gen.G

- CTBC Flying Oyster vs Team Secret Whales (Swiss Round 4, Bo3): CTBC Flying Oyster 2-0
  - Base single-game win probability for CTBC Flying Oyster: 0.510 (series win probability 0.515)
  - Game 1: multiplier 0.845, adjusted P(CTBC Flying Oyster) = 0.431, winner = CTBC Flying Oyster
  - Game 2: multiplier 1.107, adjusted P(CTBC Flying Oyster) = 0.565, winner = CTBC Flying Oyster

- 100 Thieves vs Movistar KOI (Swiss Round 4, Bo3): 100 Thieves 2-0
  - Base single-game win probability for 100 Thieves: 0.405 (series win probability 0.359)
  - Game 1: multiplier 1.164, adjusted P(100 Thieves) = 0.471, winner = 100 Thieves
  - Game 2: multiplier 1.178, adjusted P(100 Thieves) = 0.477, winner = 100 Thieves

- Bilibili Gaming vs FlyQuest (Swiss Round 4, Bo3): Bilibili Gaming 2-0
  - Base single-game win probability for Bilibili Gaming: 0.769 (series win probability 0.865)
  - Game 1: multiplier 1.030, adjusted P(Bilibili Gaming) = 0.792, winner = Bilibili Gaming
  - Game 2: multiplier 1.003, adjusted P(Bilibili Gaming) = 0.771, winner = Bilibili Gaming

- Fnatic vs G2 Esports (Swiss Round 4, Bo3): G2 Esports 2-1
  - Base single-game win probability for Fnatic: 0.422 (series win probability 0.384)
  - Game 1: multiplier 0.831, adjusted P(Fnatic) = 0.351, winner = G2 Esports
  - Game 2: multiplier 1.048, adjusted P(Fnatic) = 0.442, winner = Fnatic
  - Game 3: multiplier 1.192, adjusted P(Fnatic) = 0.503, winner = G2 Esports

- PSG Talon vs Invictus Gaming (Swiss Round 4, Bo3): Invictus Gaming 2-0
  - Base single-game win probability for PSG Talon: 0.390 (series win probability 0.338)
  - Game 1: multiplier 0.886, adjusted P(PSG Talon) = 0.346, winner = Invictus Gaming
  - Game 2: multiplier 1.131, adjusted P(PSG Talon) = 0.442, winner = Invictus Gaming

- Movistar KOI vs G2 Esports (Swiss Round 5, Bo3): G2 Esports 2-1
  - Base single-game win probability for Movistar KOI: 0.468 (series win probability 0.452)
  - Game 1: multiplier 1.049, adjusted P(Movistar KOI) = 0.491, winner = G2 Esports
  - Game 2: multiplier 0.838, adjusted P(Movistar KOI) = 0.392, winner = Movistar KOI
  - Game 3: multiplier 1.122, adjusted P(Movistar KOI) = 0.525, winner = G2 Esports

- Hanwha Life Esports vs Team Secret Whales (Swiss Round 5, Bo3): Hanwha Life Esports 2-0
  - Base single-game win probability for Hanwha Life Esports: 0.833 (series win probability 0.926)
  - Game 1: multiplier 1.009, adjusted P(Hanwha Life Esports) = 0.840, winner = Hanwha Life Esports
  - Game 2: multiplier 1.163, adjusted P(Hanwha Life Esports) = 0.969, winner = Hanwha Life Esports

- Bilibili Gaming vs Invictus Gaming (Swiss Round 5, Bo3): Invictus Gaming 2-1
  - Base single-game win probability for Bilibili Gaming: 0.676 (series win probability 0.753)
  - Game 1: multiplier 0.881, adjusted P(Bilibili Gaming) = 0.595, winner = Bilibili Gaming
  - Game 2: multiplier 1.144, adjusted P(Bilibili Gaming) = 0.773, winner = Invictus Gaming
  - Game 3: multiplier 0.900, adjusted P(Bilibili Gaming) = 0.608, winner = Invictus Gaming

### Swiss Records

| Team | Record | Outcome |
| --- | --- | --- |
| Anyone's Legend | 3-0 | Advanced |
| Top Esports | 3-0 | Advanced |
| 100 Thieves | 3-1 | Advanced |
| CTBC Flying Oyster | 3-1 | Advanced |
| Gen.G | 3-1 | Advanced |
| G2 Esports | 3-2 | Advanced |
| Hanwha Life Esports | 3-2 | Advanced |
| Invictus Gaming | 3-2 | Advanced |
| Bilibili Gaming | 2-3 | Eliminated |
| Movistar KOI | 2-3 | Eliminated |
| Team Secret Whales | 2-3 | Eliminated |
| FlyQuest | 1-3 | Eliminated |
| Fnatic | 1-3 | Eliminated |
| PSG Talon | 1-3 | Eliminated |
| KT Rolster | 0-3 | Eliminated |
| Vivo Keyd Stars | 0-3 | Eliminated |

## Knockout Stage

### Quarterfinal Draw

- Anyone's Legend vs G2 Esports
- Top Esports vs Hanwha Life Esports
- 100 Thieves vs Invictus Gaming
- CTBC Flying Oyster vs Gen.G

- Anyone's Legend vs G2 Esports (Knockout Quarterfinal 1, Bo5): Anyone's Legend 3-0
  - Base single-game win probability for Anyone's Legend: 0.679 (series win probability 0.808)
  - Game 1: multiplier 0.938, adjusted P(Anyone's Legend) = 0.637, winner = Anyone's Legend
  - Game 2: multiplier 1.007, adjusted P(Anyone's Legend) = 0.684, winner = Anyone's Legend
  - Game 3: multiplier 1.037, adjusted P(Anyone's Legend) = 0.704, winner = Anyone's Legend

- Top Esports vs Hanwha Life Esports (Knockout Quarterfinal 2, Bo5): Hanwha Life Esports 3-1
  - Base single-game win probability for Top Esports: 0.408 (series win probability 0.332)
  - Game 1: multiplier 1.120, adjusted P(Top Esports) = 0.457, winner = Hanwha Life Esports
  - Game 2: multiplier 0.819, adjusted P(Top Esports) = 0.334, winner = Hanwha Life Esports
  - Game 3: multiplier 1.123, adjusted P(Top Esports) = 0.459, winner = Top Esports
  - Game 4: multiplier 0.908, adjusted P(Top Esports) = 0.371, winner = Hanwha Life Esports

- 100 Thieves vs Invictus Gaming (Knockout Quarterfinal 3, Bo5): Invictus Gaming 3-0
  - Base single-game win probability for 100 Thieves: 0.304 (series win probability 0.168)
  - Game 1: multiplier 1.035, adjusted P(100 Thieves) = 0.315, winner = Invictus Gaming
  - Game 2: multiplier 0.886, adjusted P(100 Thieves) = 0.269, winner = Invictus Gaming
  - Game 3: multiplier 0.823, adjusted P(100 Thieves) = 0.250, winner = Invictus Gaming

- CTBC Flying Oyster vs Gen.G (Knockout Quarterfinal 4, Bo5): Gen.G 3-0
  - Base single-game win probability for CTBC Flying Oyster: 0.150 (series win probability 0.027)
  - Game 1: multiplier 1.082, adjusted P(CTBC Flying Oyster) = 0.162, winner = Gen.G
  - Game 2: multiplier 1.087, adjusted P(CTBC Flying Oyster) = 0.163, winner = Gen.G
  - Game 3: multiplier 1.164, adjusted P(CTBC Flying Oyster) = 0.174, winner = Gen.G

- Hanwha Life Esports vs Invictus Gaming (Knockout Semifinal 1, Bo5): Invictus Gaming 3-0
  - Base single-game win probability for Hanwha Life Esports: 0.728 (series win probability 0.872)
  - Game 1: multiplier 0.919, adjusted P(Hanwha Life Esports) = 0.669, winner = Invictus Gaming
  - Game 2: multiplier 1.138, adjusted P(Hanwha Life Esports) = 0.828, winner = Invictus Gaming
  - Game 3: multiplier 1.020, adjusted P(Hanwha Life Esports) = 0.743, winner = Invictus Gaming

- Anyone's Legend vs Gen.G (Knockout Semifinal 2, Bo5): Gen.G 3-0
  - Base single-game win probability for Anyone's Legend: 0.327 (series win probability 0.201)
  - Game 1: multiplier 0.808, adjusted P(Anyone's Legend) = 0.264, winner = Gen.G
  - Game 2: multiplier 1.072, adjusted P(Anyone's Legend) = 0.351, winner = Gen.G
  - Game 3: multiplier 1.067, adjusted P(Anyone's Legend) = 0.349, winner = Gen.G

- Invictus Gaming vs Gen.G (Knockout Grand Final, Bo5): Gen.G 3-0
  - Base single-game win probability for Invictus Gaming: 0.240 (series win probability 0.093)
  - Game 1: multiplier 1.134, adjusted P(Invictus Gaming) = 0.272, winner = Gen.G
  - Game 2: multiplier 1.188, adjusted P(Invictus Gaming) = 0.285, winner = Gen.G
  - Game 3: multiplier 1.081, adjusted P(Invictus Gaming) = 0.259, winner = Gen.G

### Podium

- Champion: Gen.G
- Runner-up: Invictus Gaming
