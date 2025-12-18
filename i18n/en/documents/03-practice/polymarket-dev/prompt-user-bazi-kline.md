# Life K-Line LLM User Prompt Template (Full Original Text)

This file is extracted from the `userPrompt` assembly logic in `libs/external/web/lifekline-main/services/geminiService.ts`, and has been replaced with template variables for direct reuse.

```
Please analyze based on the **already arranged** Four Pillars of Destiny (Bazi) and the **specified Grand Cycle information**.
    
【Basic Information】
Gender：${genderStr}
Name：${input.name || "Not Provided"}
Birth Year：${input.birthYear} (Solar Calendar)
    
【Four Pillars of Destiny】
Year Pillar：${input.yearPillar} (Heavenly Stem Polarity：${yearStemPolarity === 'YANG' ? 'Yang' : 'Yin'})
Month Pillar：${input.monthPillar}
Day Pillar：${input.dayPillar}
Hour Pillar：${input.hourPillar}
    
【Grand Cycle Core Parameters】
1. Starting Age of Grand Cycle：${input.startAge} (Nominal Age).
2. First Step of Grand Cycle：${input.firstDaYun}.
3. **Sorting Direction**：${daYunDirectionStr}.
    
【Algorithms that Must Be Executed - Grand Cycle Sequence Generation】
Please strictly follow the steps below to generate data：
    
1. **Lock the First Step**：Confirm [${input.firstDaYun}] as the first step of the Grand Cycle.
2. **Calculate Sequence**：Based on the sixty Jiazi sequence and direction (${daYunDirectionStr}), deduce the next 9 steps of the Grand Cycle.
   ${directionExample}
3. **Fill JSON**：
   - Age 1 to ${startAgeInt - 1}: daYun = "Childhood"
   - Age ${startAgeInt} to ${startAgeInt + 9}: daYun = [1st Step Grand Cycle: ${input.firstDaYun}]
   - Age ${startAgeInt + 10} to ${startAgeInt + 19}: daYun = [2nd Step Grand Cycle]
   - Age ${startAgeInt + 20} to ${startAgeInt + 29}: daYun = [3rd Step Grand Cycle]
   - ...and so on until 100 years old.
    
【Special Warning】
- **daYun field**：Must fill in the Grand Cycle Heavenly Stems and Earthly Branches (changes every 10 years), **absolutely do not** fill in the Annual Cycle Heavenly Stems and Earthly Branches.
- **ganZhi field**：Fill in the **Annual Cycle Heavenly Stems and Earthly Branches** for that year (changes every year, e.g., 2024=Jia Chen, 2025=Yi Si).
    
Task：
1. Confirm the格局 and喜忌 (patterns and favorable/unfavorable elements).
2. Generate Life Annual K-Line data for **ages 1-100 (nominal age)**.
3. Provide detailed annual commentary in the `reason` field.
4. Generate a numerology analysis report with scores (including personality analysis, crypto trading analysis, and development feng shui analysis).
    
Please strictly follow the system instructions to generate JSON data.
```

# Instructions
- Pass as a `user` message to `/chat/completions`, used in conjunction with the system prompt.
- Variable meanings: `genderStr` is composed of gender + Qiankun text; `startAgeInt` is the integer of the starting age; `directionExample` changes with顺/逆行 (forward/reverse movement); other variables are directly taken from user input or chart results.
- The output must be pure JSON, `geminiService` will automatically strip code blocks and validate `chartPoints`.
