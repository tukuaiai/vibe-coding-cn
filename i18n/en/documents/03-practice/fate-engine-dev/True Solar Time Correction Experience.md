# True Solar Time Correction Experience (2025-12-16)

## Background
- Feedback from Xinjiang users: The report shows "solar calendar minus 2 hours, true solar time again minus 2 hours", resulting in inconsistencies in Four Pillars/Deities with comparison tools.
- Root cause: Birth time was calculated once for true solar time by the caller, and then calculated again within `BaziCalculator`, forming a "double deduction".

## Current Strategy (Live)
- **Single Correction Point**: All true solar time corrections are performed only once within `BaziCalculator`.
- **Time Baseline**: Entry birth time is uniformly treated as Beijing Time (Asia/Shanghai), and then true solar time correction is performed after assigning the time zone with `ensure_cn`.
- **Calculation Time**: Core and extended modules are all based on `calc_dt` (true solar time or original Beijing time if user disables), maintaining consistency.
- **Display Time**: UI/progress/logs/queue/Help uniformly use Beijing Time; report field `trueSolarTime` displays the time after longitude correction.

## Involved Changes (Key Points)
- `utils/timezone.py`: `now_cn/ensure_cn/fmt_cn` fixed to Asia/Shanghai.
- `bot.py`: Removed outer layer `calc_true_solar_time`; time display uses `fmt_cn(now_cn())`; queue timestamp uses Beijing Time.
- `main.py`: API no longer pre-corrects; `trueSolarTime` is taken from `BaziCalculator` internal results.
- `bazi_calculator.py`: Added `use_true_solar_time`, unified `calc_dt`; extended modules/Ming Gua/Xiao Yun, etc., now use `calc_dt`; metadata time uses Beijing Time.
- `liuyao.py`, `qimen.py`, `system_optimization.py`: Timestamps unified to Beijing Time.
- Documentation: `AGENTS.md` records "Time zone unified to Asia/Shanghai".

## Abstract Problems and Prevention
1.  **Inconsistent Time Zone Assumptions**: Naive datetime will drift if parsed locally; uniformly assume "input is Beijing Time", first supplement time zone, then calculate.
2.  **Duplicate Correction**: True solar time formula is only allowed to appear once; secondary correction is strictly prohibited in the call chain.
3.  **Mixed Baselines**: Display uses Beijing Time, calculation uses true solar time (single correction). If a new module is added, `calc_dt` must be reused, no self-calculation is allowed.

## Verification Suggestions
- Run a Xinjiang example (Urumqi 87E, 08:00): Solar calendar should remain 08:00, Beijing time displays 08:00, true solar time approx. 05:4x, only deducted once.
- Compare Four Pillars/Deities with comparison tools such as "Cece", should be consistent.

## Subsequent Guidelines
- If UTC/other time zones need to be provided externally, first convert to Beijing time, then calculate true solar time based on longitude, still only correcting once.
- When adding new integration modules, it is forbidden to repeatedly calculate true solar time; uniformly accept `calc_dt`.
