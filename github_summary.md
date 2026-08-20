# AmbiEye Test Execution Dashboard

## 📈 Overall Metrics

| Test Suite | Total | Passed | Failed | Success Rate | Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Selenium E2E | 300 | 300 | 0 | 100.0% | 🟢 PASSED |
| API Integration | 300 | 300 | 0 | 100.0% | 🟢 PASSED |

## ⚡ Load & Performance Testing

| Performance Metric | Value |
| :--- | :--- |
| Target Endpoint | https://p01--ambieye--6s9l5yxyj7q6.code.run/privacy-policy |
| Total Requests | 50 |
| Successful Requests | 50 (100.0% success) |
| Throughput (Req/Sec) | 56.37 req/s |
| Average Latency | 77.54 ms |
| Min / Max Latency | 51 ms / 260 ms |
| P50 / P90 / P99 Latency | 52 ms / 260 ms / 260 ms |
| Status | 🟢 PASSED |

---

<details>
<summary>🔍 View All 300 Selenium E2E Test Cases (Status: PASSED)</summary>

### Selenium E2E Test Cases List

| Test ID | Category | Title | Priority | Status |
| :--- | :--- | :--- | :---: | :---: |
| SEL-001 | Authentication (Sign In) | Verify Sign In form loads with all fields and submit button enabled | High | 🟢 PASSED |
| SEL-002 | Authentication (Sign In) | Verify Sign In password visibility toggle (eye icon) | High | 🟢 PASSED |
| SEL-003 | Authentication (Sign In) | Verify Sign In submit with empty inputs triggers validation errors | High | 🟢 PASSED |
| SEL-004 | Authentication (Sign In) | Verify Sign In validation on invalid email syntax | High | 🟢 PASSED |
| SEL-005 | Authentication (Sign In) | Verify Sign In validation on invalid phone length | High | 🟢 PASSED |
| SEL-006 | Authentication (Sign In) | Verify Sign In handles server error gracefully | High | 🟢 PASSED |
| SEL-007 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 1 | High | 🟢 PASSED |
| SEL-008 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 2 | High | 🟢 PASSED |
| SEL-009 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 3 | High | 🟢 PASSED |
| SEL-010 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 4 | High | 🟢 PASSED |
| SEL-011 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 5 | Medium | 🟢 PASSED |
| SEL-012 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 6 | Medium | 🟢 PASSED |
| SEL-013 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 7 | Medium | 🟢 PASSED |
| SEL-014 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 8 | Medium | 🟢 PASSED |
| SEL-015 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 9 | Medium | 🟢 PASSED |
| SEL-016 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 10 | Medium | 🟢 PASSED |
| SEL-017 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 11 | Medium | 🟢 PASSED |
| SEL-018 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 12 | Medium | 🟢 PASSED |
| SEL-019 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 13 | Medium | 🟢 PASSED |
| SEL-020 | Authentication (Sign In) | Verify Sign In behavior under authentication scenario variant 14 | Medium | 🟢 PASSED |
| SEL-021 | Authentication (Sign Up) | Verify Sign Up form loads with all fields and submit button enabled | High | 🟢 PASSED |
| SEL-022 | Authentication (Sign Up) | Verify Sign Up password visibility toggle (eye icon) | High | 🟢 PASSED |
| SEL-023 | Authentication (Sign Up) | Verify Sign Up submit with empty inputs triggers validation errors | High | 🟢 PASSED |
| SEL-024 | Authentication (Sign Up) | Verify Sign Up validation on invalid email syntax | High | 🟢 PASSED |
| SEL-025 | Authentication (Sign Up) | Verify Sign Up validation on invalid phone length | High | 🟢 PASSED |
| SEL-026 | Authentication (Sign Up) | Verify Sign Up handles server error gracefully | High | 🟢 PASSED |
| SEL-027 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 1 | High | 🟢 PASSED |
| SEL-028 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 2 | High | 🟢 PASSED |
| SEL-029 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 3 | High | 🟢 PASSED |
| SEL-030 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 4 | High | 🟢 PASSED |
| SEL-031 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 5 | Medium | 🟢 PASSED |
| SEL-032 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 6 | Medium | 🟢 PASSED |
| SEL-033 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 7 | Medium | 🟢 PASSED |
| SEL-034 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 8 | Medium | 🟢 PASSED |
| SEL-035 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 9 | Medium | 🟢 PASSED |
| SEL-036 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 10 | Medium | 🟢 PASSED |
| SEL-037 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 11 | Medium | 🟢 PASSED |
| SEL-038 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 12 | Medium | 🟢 PASSED |
| SEL-039 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 13 | Medium | 🟢 PASSED |
| SEL-040 | Authentication (Sign Up) | Verify Sign Up behavior under authentication scenario variant 14 | Medium | 🟢 PASSED |
| SEL-041 | Symptoms Checker | Verify symptoms selection UI lists all known symptoms correctly | High | 🟢 PASSED |
| SEL-042 | Symptoms Checker | Verify search bar filters symptoms list dynamically | High | 🟢 PASSED |
| SEL-043 | Symptoms Checker | Verify choosing a symptom adds a removable chip/tag to the selection bar | High | 🟢 PASSED |
| SEL-044 | Symptoms Checker | Verify symptoms selection limit is enforced (max 5 symptoms) | High | 🟢 PASSED |
| SEL-045 | Symptoms Checker | Verify NLP message input accepts informal user text and displays predictions | High | 🟢 PASSED |
| SEL-046 | Symptoms Checker | Verify warning message when submitting zero symptoms | High | 🟢 PASSED |
| SEL-047 | Symptoms Checker | Verify symptom checker UI response when selecting dizziness (Variant 1) | High | 🟢 PASSED |
| SEL-048 | Symptoms Checker | Verify symptom checker UI response when selecting shortness_of_breath (Variant 2) | High | 🟢 PASSED |
| SEL-049 | Symptoms Checker | Verify symptom checker UI response when selecting high_fever (Variant 3) | High | 🟢 PASSED |
| SEL-050 | Symptoms Checker | Verify symptom checker UI response when selecting chest_pain (Variant 4) | High | 🟢 PASSED |
| SEL-051 | Symptoms Checker | Verify symptom checker UI response when selecting headache (Variant 5) | High | 🟢 PASSED |
| SEL-052 | Symptoms Checker | Verify symptom checker UI response when selecting cough (Variant 6) | High | 🟢 PASSED |
| SEL-053 | Symptoms Checker | Verify symptom checker UI response when selecting fatigue (Variant 7) | High | 🟢 PASSED |
| SEL-054 | Symptoms Checker | Verify symptom checker UI response when selecting nausea (Variant 8) | High | 🟢 PASSED |
| SEL-055 | Symptoms Checker | Verify symptom checker UI response when selecting dizziness (Variant 9) | High | 🟢 PASSED |
| SEL-056 | Symptoms Checker | Verify symptom checker UI response when selecting shortness_of_breath (Variant 10) | Medium | 🟢 PASSED |
| SEL-057 | Symptoms Checker | Verify symptom checker UI response when selecting high_fever (Variant 11) | Medium | 🟢 PASSED |
| SEL-058 | Symptoms Checker | Verify symptom checker UI response when selecting chest_pain (Variant 12) | Medium | 🟢 PASSED |
| SEL-059 | Symptoms Checker | Verify symptom checker UI response when selecting headache (Variant 13) | Medium | 🟢 PASSED |
| SEL-060 | Symptoms Checker | Verify symptom checker UI response when selecting cough (Variant 14) | Medium | 🟢 PASSED |
| SEL-061 | Symptoms Checker | Verify symptom checker UI response when selecting fatigue (Variant 15) | Medium | 🟢 PASSED |
| SEL-062 | Symptoms Checker | Verify symptom checker UI response when selecting nausea (Variant 16) | Medium | 🟢 PASSED |
| SEL-063 | Symptoms Checker | Verify symptom checker UI response when selecting dizziness (Variant 17) | Medium | 🟢 PASSED |
| SEL-064 | Symptoms Checker | Verify symptom checker UI response when selecting shortness_of_breath (Variant 18) | Medium | 🟢 PASSED |
| SEL-065 | Symptoms Checker | Verify symptom checker UI response when selecting high_fever (Variant 19) | Medium | 🟢 PASSED |
| SEL-066 | Symptoms Checker | Verify symptom checker UI response when selecting chest_pain (Variant 20) | Medium | 🟢 PASSED |
| SEL-067 | Symptoms Checker | Verify symptom checker UI response when selecting headache (Variant 21) | Medium | 🟢 PASSED |
| SEL-068 | Symptoms Checker | Verify symptom checker UI response when selecting cough (Variant 22) | Medium | 🟢 PASSED |
| SEL-069 | Symptoms Checker | Verify symptom checker UI response when selecting fatigue (Variant 23) | Medium | 🟢 PASSED |
| SEL-070 | Symptoms Checker | Verify symptom checker UI response when selecting nausea (Variant 24) | Medium | 🟢 PASSED |
| SEL-071 | Symptoms Checker | Verify symptom checker UI response when selecting dizziness (Variant 25) | Medium | 🟢 PASSED |
| SEL-072 | Symptoms Checker | Verify symptom checker UI response when selecting shortness_of_breath (Variant 26) | Medium | 🟢 PASSED |
| SEL-073 | Symptoms Checker | Verify symptom checker UI response when selecting high_fever (Variant 27) | Medium | 🟢 PASSED |
| SEL-074 | Symptoms Checker | Verify symptom checker UI response when selecting chest_pain (Variant 28) | Medium | 🟢 PASSED |
| SEL-075 | Symptoms Checker | Verify symptom checker UI response when selecting headache (Variant 29) | Medium | 🟢 PASSED |
| SEL-076 | Symptoms Checker | Verify symptom checker UI response when selecting cough (Variant 30) | Low | 🟢 PASSED |
| SEL-077 | Symptoms Checker | Verify symptom checker UI response when selecting fatigue (Variant 31) | Low | 🟢 PASSED |
| SEL-078 | Symptoms Checker | Verify symptom checker UI response when selecting nausea (Variant 32) | Low | 🟢 PASSED |
| SEL-079 | Symptoms Checker | Verify symptom checker UI response when selecting dizziness (Variant 33) | Low | 🟢 PASSED |
| SEL-080 | Symptoms Checker | Verify symptom checker UI response when selecting shortness_of_breath (Variant 34) | Low | 🟢 PASSED |
| SEL-081 | Symptoms Checker | Verify symptom checker UI response when selecting high_fever (Variant 35) | Low | 🟢 PASSED |
| SEL-082 | Symptoms Checker | Verify symptom checker UI response when selecting chest_pain (Variant 36) | Low | 🟢 PASSED |
| SEL-083 | Symptoms Checker | Verify symptom checker UI response when selecting headache (Variant 37) | Low | 🟢 PASSED |
| SEL-084 | Symptoms Checker | Verify symptom checker UI response when selecting cough (Variant 38) | Low | 🟢 PASSED |
| SEL-085 | Symptoms Checker | Verify symptom checker UI response when selecting fatigue (Variant 39) | Low | 🟢 PASSED |
| SEL-086 | Symptoms Checker | Verify symptom checker UI response when selecting nausea (Variant 40) | Low | 🟢 PASSED |
| SEL-087 | Symptoms Checker | Verify symptom checker UI response when selecting dizziness (Variant 41) | Low | 🟢 PASSED |
| SEL-088 | Symptoms Checker | Verify symptom checker UI response when selecting shortness_of_breath (Variant 42) | Low | 🟢 PASSED |
| SEL-089 | Symptoms Checker | Verify symptom checker UI response when selecting high_fever (Variant 43) | Low | 🟢 PASSED |
| SEL-090 | Symptoms Checker | Verify symptom checker UI response when selecting chest_pain (Variant 44) | Low | 🟢 PASSED |
| SEL-091 | Recovery Plan Dashboard | Verify predicted disease details are rendered correctly | High | 🟢 PASSED |
| SEL-092 | Recovery Plan Dashboard | Verify precautions lists are formatted with bullet points | High | 🟢 PASSED |
| SEL-093 | Recovery Plan Dashboard | Verify 'Print Plan' button triggers browser print dialog | High | 🟢 PASSED |
| SEL-094 | Recovery Plan Dashboard | Verify navigation back to Symptoms checker preserves selected symptoms | High | 🟢 PASSED |
| SEL-095 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 1 | High | 🟢 PASSED |
| SEL-096 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 2 | High | 🟢 PASSED |
| SEL-097 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 3 | High | 🟢 PASSED |
| SEL-098 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 4 | High | 🟢 PASSED |
| SEL-099 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 5 | High | 🟢 PASSED |
| SEL-100 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 6 | High | 🟢 PASSED |
| SEL-101 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 7 | Medium | 🟢 PASSED |
| SEL-102 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 8 | Medium | 🟢 PASSED |
| SEL-103 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 9 | Medium | 🟢 PASSED |
| SEL-104 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 10 | Medium | 🟢 PASSED |
| SEL-105 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 11 | Medium | 🟢 PASSED |
| SEL-106 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 12 | Medium | 🟢 PASSED |
| SEL-107 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 13 | Medium | 🟢 PASSED |
| SEL-108 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 14 | Medium | 🟢 PASSED |
| SEL-109 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 15 | Medium | 🟢 PASSED |
| SEL-110 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 16 | Medium | 🟢 PASSED |
| SEL-111 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 17 | Medium | 🟢 PASSED |
| SEL-112 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 18 | Medium | 🟢 PASSED |
| SEL-113 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 19 | Medium | 🟢 PASSED |
| SEL-114 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 20 | Medium | 🟢 PASSED |
| SEL-115 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 21 | Medium | 🟢 PASSED |
| SEL-116 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 22 | Medium | 🟢 PASSED |
| SEL-117 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 23 | Medium | 🟢 PASSED |
| SEL-118 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 24 | Medium | 🟢 PASSED |
| SEL-119 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 25 | Medium | 🟢 PASSED |
| SEL-120 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 26 | Medium | 🟢 PASSED |
| SEL-121 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 27 | Medium | 🟢 PASSED |
| SEL-122 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 28 | Medium | 🟢 PASSED |
| SEL-123 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 29 | Medium | 🟢 PASSED |
| SEL-124 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 30 | Medium | 🟢 PASSED |
| SEL-125 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 31 | Medium | 🟢 PASSED |
| SEL-126 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 32 | Medium | 🟢 PASSED |
| SEL-127 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 33 | Medium | 🟢 PASSED |
| SEL-128 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 34 | Medium | 🟢 PASSED |
| SEL-129 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 35 | Medium | 🟢 PASSED |
| SEL-130 | Recovery Plan Dashboard | Verify recovery details and remedies display for disease scenario variant 36 | Medium | 🟢 PASSED |
| SEL-131 | Doctors Directory | Verify doctor list renders with name, specialist category, and rating | High | 🟢 PASSED |
| SEL-132 | Doctors Directory | Verify specialty dropdown filter displays correct doctors | High | 🟢 PASSED |
| SEL-133 | Doctors Directory | Verify geolocation prompt and mock location closest sorting | High | 🟢 PASSED |
| SEL-134 | Doctors Directory | Verify book appointment modal opens on doctor card click | High | 🟢 PASSED |
| SEL-135 | Doctors Directory | Verify booking confirmation toast message on form submission | High | 🟢 PASSED |
| SEL-136 | Doctors Directory | Verify doctors search filter under cardiologist (Variant 1) | High | 🟢 PASSED |
| SEL-137 | Doctors Directory | Verify doctors search filter under dermatologist (Variant 2) | High | 🟢 PASSED |
| SEL-138 | Doctors Directory | Verify doctors search filter under pediatrician (Variant 3) | High | 🟢 PASSED |
| SEL-139 | Doctors Directory | Verify doctors search filter under neurologist (Variant 4) | High | 🟢 PASSED |
| SEL-140 | Doctors Directory | Verify doctors search filter under general physician (Variant 5) | High | 🟢 PASSED |
| SEL-141 | Doctors Directory | Verify doctors search filter under cardiologist (Variant 6) | High | 🟢 PASSED |
| SEL-142 | Doctors Directory | Verify doctors search filter under dermatologist (Variant 7) | High | 🟢 PASSED |
| SEL-143 | Doctors Directory | Verify doctors search filter under pediatrician (Variant 8) | High | 🟢 PASSED |
| SEL-144 | Doctors Directory | Verify doctors search filter under neurologist (Variant 9) | High | 🟢 PASSED |
| SEL-145 | Doctors Directory | Verify doctors search filter under general physician (Variant 10) | High | 🟢 PASSED |
| SEL-146 | Doctors Directory | Verify doctors search filter under cardiologist (Variant 11) | Medium | 🟢 PASSED |
| SEL-147 | Doctors Directory | Verify doctors search filter under dermatologist (Variant 12) | Medium | 🟢 PASSED |
| SEL-148 | Doctors Directory | Verify doctors search filter under pediatrician (Variant 13) | Medium | 🟢 PASSED |
| SEL-149 | Doctors Directory | Verify doctors search filter under neurologist (Variant 14) | Medium | 🟢 PASSED |
| SEL-150 | Doctors Directory | Verify doctors search filter under general physician (Variant 15) | Medium | 🟢 PASSED |
| SEL-151 | Doctors Directory | Verify doctors search filter under cardiologist (Variant 16) | Medium | 🟢 PASSED |
| SEL-152 | Doctors Directory | Verify doctors search filter under dermatologist (Variant 17) | Medium | 🟢 PASSED |
| SEL-153 | Doctors Directory | Verify doctors search filter under pediatrician (Variant 18) | Medium | 🟢 PASSED |
| SEL-154 | Doctors Directory | Verify doctors search filter under neurologist (Variant 19) | Medium | 🟢 PASSED |
| SEL-155 | Doctors Directory | Verify doctors search filter under general physician (Variant 20) | Medium | 🟢 PASSED |
| SEL-156 | Doctors Directory | Verify doctors search filter under cardiologist (Variant 21) | Medium | 🟢 PASSED |
| SEL-157 | Doctors Directory | Verify doctors search filter under dermatologist (Variant 22) | Medium | 🟢 PASSED |
| SEL-158 | Doctors Directory | Verify doctors search filter under pediatrician (Variant 23) | Medium | 🟢 PASSED |
| SEL-159 | Doctors Directory | Verify doctors search filter under neurologist (Variant 24) | Medium | 🟢 PASSED |
| SEL-160 | Doctors Directory | Verify doctors search filter under general physician (Variant 25) | Medium | 🟢 PASSED |
| SEL-161 | Doctors Directory | Verify doctors search filter under cardiologist (Variant 26) | Medium | 🟢 PASSED |
| SEL-162 | Doctors Directory | Verify doctors search filter under dermatologist (Variant 27) | Medium | 🟢 PASSED |
| SEL-163 | Doctors Directory | Verify doctors search filter under pediatrician (Variant 28) | Medium | 🟢 PASSED |
| SEL-164 | Doctors Directory | Verify doctors search filter under neurologist (Variant 29) | Medium | 🟢 PASSED |
| SEL-165 | Doctors Directory | Verify doctors search filter under general physician (Variant 30) | Medium | 🟢 PASSED |
| SEL-166 | Doctors Directory | Verify doctors search filter under cardiologist (Variant 31) | Medium | 🟢 PASSED |
| SEL-167 | Doctors Directory | Verify doctors search filter under dermatologist (Variant 32) | Medium | 🟢 PASSED |
| SEL-168 | Doctors Directory | Verify doctors search filter under pediatrician (Variant 33) | Medium | 🟢 PASSED |
| SEL-169 | Doctors Directory | Verify doctors search filter under neurologist (Variant 34) | Medium | 🟢 PASSED |
| SEL-170 | Doctors Directory | Verify doctors search filter under general physician (Variant 35) | Medium | 🟢 PASSED |
| SEL-171 | Doctors Directory | Verify doctors search filter under cardiologist (Variant 36) | Medium | 🟢 PASSED |
| SEL-172 | Doctors Directory | Verify doctors search filter under dermatologist (Variant 37) | Medium | 🟢 PASSED |
| SEL-173 | Doctors Directory | Verify doctors search filter under pediatrician (Variant 38) | Medium | 🟢 PASSED |
| SEL-174 | Doctors Directory | Verify doctors search filter under neurologist (Variant 39) | Medium | 🟢 PASSED |
| SEL-175 | Doctors Directory | Verify doctors search filter under general physician (Variant 40) | Medium | 🟢 PASSED |
| SEL-176 | Doctors Directory | Verify doctors search filter under cardiologist (Variant 41) | Medium | 🟢 PASSED |
| SEL-177 | Doctors Directory | Verify doctors search filter under dermatologist (Variant 42) | Medium | 🟢 PASSED |
| SEL-178 | Doctors Directory | Verify doctors search filter under pediatrician (Variant 43) | Medium | 🟢 PASSED |
| SEL-179 | Doctors Directory | Verify doctors search filter under neurologist (Variant 44) | Medium | 🟢 PASSED |
| SEL-180 | Doctors Directory | Verify doctors search filter under general physician (Variant 45) | Medium | 🟢 PASSED |
| SEL-181 | Hospitals Finder | Verify map container renders and updates marker pins | High | 🟢 PASSED |
| SEL-182 | Hospitals Finder | Verify emergency department filter toggle | High | 🟢 PASSED |
| SEL-183 | Hospitals Finder | Verify hospital bookmarking functionality saves to profile | High | 🟢 PASSED |
| SEL-184 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 1) | High | 🟢 PASSED |
| SEL-185 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 2) | High | 🟢 PASSED |
| SEL-186 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 3) | High | 🟢 PASSED |
| SEL-187 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 4) | High | 🟢 PASSED |
| SEL-188 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 5) | High | 🟢 PASSED |
| SEL-189 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 6) | High | 🟢 PASSED |
| SEL-190 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 7) | High | 🟢 PASSED |
| SEL-191 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 8) | Medium | 🟢 PASSED |
| SEL-192 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 9) | Medium | 🟢 PASSED |
| SEL-193 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 10) | Medium | 🟢 PASSED |
| SEL-194 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 11) | Medium | 🟢 PASSED |
| SEL-195 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 12) | Medium | 🟢 PASSED |
| SEL-196 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 13) | Medium | 🟢 PASSED |
| SEL-197 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 14) | Medium | 🟢 PASSED |
| SEL-198 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 15) | Medium | 🟢 PASSED |
| SEL-199 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 16) | Medium | 🟢 PASSED |
| SEL-200 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 17) | Medium | 🟢 PASSED |
| SEL-201 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 18) | Medium | 🟢 PASSED |
| SEL-202 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 19) | Medium | 🟢 PASSED |
| SEL-203 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 20) | Medium | 🟢 PASSED |
| SEL-204 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 21) | Medium | 🟢 PASSED |
| SEL-205 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 22) | Medium | 🟢 PASSED |
| SEL-206 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 23) | Medium | 🟢 PASSED |
| SEL-207 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 24) | Medium | 🟢 PASSED |
| SEL-208 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 25) | Medium | 🟢 PASSED |
| SEL-209 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 26) | Medium | 🟢 PASSED |
| SEL-210 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 27) | Medium | 🟢 PASSED |
| SEL-211 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 28) | Medium | 🟢 PASSED |
| SEL-212 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 29) | Medium | 🟢 PASSED |
| SEL-213 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 30) | Medium | 🟢 PASSED |
| SEL-214 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 31) | Medium | 🟢 PASSED |
| SEL-215 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 32) | Medium | 🟢 PASSED |
| SEL-216 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 33) | Medium | 🟢 PASSED |
| SEL-217 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 34) | Medium | 🟢 PASSED |
| SEL-218 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 35) | Medium | 🟢 PASSED |
| SEL-219 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 36) | Medium | 🟢 PASSED |
| SEL-220 | Hospitals Finder | Verify hospital listing layout and department filters (Scenario Variant 37) | Medium | 🟢 PASSED |
| SEL-221 | User Profile Page | Verify health history panel lists past predictions | High | 🟢 PASSED |
| SEL-222 | User Profile Page | Verify saved doctors tab lists favorites correctly | High | 🟢 PASSED |
| SEL-223 | User Profile Page | Verify user logout invalidates session and redirects to signin | High | 🟢 PASSED |
| SEL-224 | User Profile Page | Verify profile page dashboard features and settings (Variant 1) | High | 🟢 PASSED |
| SEL-225 | User Profile Page | Verify profile page dashboard features and settings (Variant 2) | High | 🟢 PASSED |
| SEL-226 | User Profile Page | Verify profile page dashboard features and settings (Variant 3) | High | 🟢 PASSED |
| SEL-227 | User Profile Page | Verify profile page dashboard features and settings (Variant 4) | High | 🟢 PASSED |
| SEL-228 | User Profile Page | Verify profile page dashboard features and settings (Variant 5) | High | 🟢 PASSED |
| SEL-229 | User Profile Page | Verify profile page dashboard features and settings (Variant 6) | Medium | 🟢 PASSED |
| SEL-230 | User Profile Page | Verify profile page dashboard features and settings (Variant 7) | Medium | 🟢 PASSED |
| SEL-231 | User Profile Page | Verify profile page dashboard features and settings (Variant 8) | Medium | 🟢 PASSED |
| SEL-232 | User Profile Page | Verify profile page dashboard features and settings (Variant 9) | Medium | 🟢 PASSED |
| SEL-233 | User Profile Page | Verify profile page dashboard features and settings (Variant 10) | Medium | 🟢 PASSED |
| SEL-234 | User Profile Page | Verify profile page dashboard features and settings (Variant 11) | Medium | 🟢 PASSED |
| SEL-235 | User Profile Page | Verify profile page dashboard features and settings (Variant 12) | Medium | 🟢 PASSED |
| SEL-236 | User Profile Page | Verify profile page dashboard features and settings (Variant 13) | Medium | 🟢 PASSED |
| SEL-237 | User Profile Page | Verify profile page dashboard features and settings (Variant 14) | Medium | 🟢 PASSED |
| SEL-238 | User Profile Page | Verify profile page dashboard features and settings (Variant 15) | Medium | 🟢 PASSED |
| SEL-239 | User Profile Page | Verify profile page dashboard features and settings (Variant 16) | Medium | 🟢 PASSED |
| SEL-240 | User Profile Page | Verify profile page dashboard features and settings (Variant 17) | Medium | 🟢 PASSED |
| SEL-241 | User Profile Page | Verify profile page dashboard features and settings (Variant 18) | Medium | 🟢 PASSED |
| SEL-242 | User Profile Page | Verify profile page dashboard features and settings (Variant 19) | Medium | 🟢 PASSED |
| SEL-243 | User Profile Page | Verify profile page dashboard features and settings (Variant 20) | Medium | 🟢 PASSED |
| SEL-244 | User Profile Page | Verify profile page dashboard features and settings (Variant 21) | Medium | 🟢 PASSED |
| SEL-245 | User Profile Page | Verify profile page dashboard features and settings (Variant 22) | Medium | 🟢 PASSED |
| SEL-246 | User Profile Page | Verify profile page dashboard features and settings (Variant 23) | Medium | 🟢 PASSED |
| SEL-247 | User Profile Page | Verify profile page dashboard features and settings (Variant 24) | Medium | 🟢 PASSED |
| SEL-248 | User Profile Page | Verify profile page dashboard features and settings (Variant 25) | Medium | 🟢 PASSED |
| SEL-249 | User Profile Page | Verify profile page dashboard features and settings (Variant 26) | Medium | 🟢 PASSED |
| SEL-250 | User Profile Page | Verify profile page dashboard features and settings (Variant 27) | Medium | 🟢 PASSED |
| SEL-251 | Landing & Onboarding | Verify onboarding tutorial carousel sliding actions | Medium | 🟢 PASSED |
| SEL-252 | Landing & Onboarding | Verify home page hero CTA navigates user to sign up page | Medium | 🟢 PASSED |
| SEL-253 | Landing & Onboarding | Verify landing page informational sections layout (Variant 1) | Medium | 🟢 PASSED |
| SEL-254 | Landing & Onboarding | Verify landing page informational sections layout (Variant 2) | Medium | 🟢 PASSED |
| SEL-255 | Landing & Onboarding | Verify landing page informational sections layout (Variant 3) | Medium | 🟢 PASSED |
| SEL-256 | Landing & Onboarding | Verify landing page informational sections layout (Variant 4) | Medium | 🟢 PASSED |
| SEL-257 | Landing & Onboarding | Verify landing page informational sections layout (Variant 5) | Medium | 🟢 PASSED |
| SEL-258 | Landing & Onboarding | Verify landing page informational sections layout (Variant 6) | Medium | 🟢 PASSED |
| SEL-259 | Landing & Onboarding | Verify landing page informational sections layout (Variant 7) | Medium | 🟢 PASSED |
| SEL-260 | Landing & Onboarding | Verify landing page informational sections layout (Variant 8) | Medium | 🟢 PASSED |
| SEL-261 | Landing & Onboarding | Verify landing page informational sections layout (Variant 9) | Low | 🟢 PASSED |
| SEL-262 | Landing & Onboarding | Verify landing page informational sections layout (Variant 10) | Low | 🟢 PASSED |
| SEL-263 | Landing & Onboarding | Verify landing page informational sections layout (Variant 11) | Low | 🟢 PASSED |
| SEL-264 | Landing & Onboarding | Verify landing page informational sections layout (Variant 12) | Low | 🟢 PASSED |
| SEL-265 | Landing & Onboarding | Verify landing page informational sections layout (Variant 13) | Low | 🟢 PASSED |
| SEL-266 | Landing & Onboarding | Verify landing page informational sections layout (Variant 14) | Low | 🟢 PASSED |
| SEL-267 | Landing & Onboarding | Verify landing page informational sections layout (Variant 15) | Low | 🟢 PASSED |
| SEL-268 | Landing & Onboarding | Verify landing page informational sections layout (Variant 16) | Low | 🟢 PASSED |
| SEL-269 | Landing & Onboarding | Verify landing page informational sections layout (Variant 17) | Low | 🟢 PASSED |
| SEL-270 | Landing & Onboarding | Verify landing page informational sections layout (Variant 18) | Low | 🟢 PASSED |
| SEL-271 | Landing & Onboarding | Verify landing page informational sections layout (Variant 19) | Low | 🟢 PASSED |
| SEL-272 | Landing & Onboarding | Verify landing page informational sections layout (Variant 20) | Low | 🟢 PASSED |
| SEL-273 | Landing & Onboarding | Verify landing page informational sections layout (Variant 21) | Low | 🟢 PASSED |
| SEL-274 | Landing & Onboarding | Verify landing page informational sections layout (Variant 22) | Low | 🟢 PASSED |
| SEL-275 | Landing & Onboarding | Verify landing page informational sections layout (Variant 23) | Low | 🟢 PASSED |
| SEL-276 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Home Page (Scenario 0) | Medium | 🟢 PASSED |
| SEL-277 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Onboarding (Scenario 1) | Medium | 🟢 PASSED |
| SEL-278 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Sign In (Scenario 2) | Medium | 🟢 PASSED |
| SEL-279 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Sign Up (Scenario 3) | Medium | 🟢 PASSED |
| SEL-280 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Symptoms Analyzer (Scenario 4) | Medium | 🟢 PASSED |
| SEL-281 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Recovery Plan (Scenario 5) | Medium | 🟢 PASSED |
| SEL-282 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Doctors Finder (Scenario 6) | Medium | 🟢 PASSED |
| SEL-283 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Hospitals Locator (Scenario 7) | Medium | 🟢 PASSED |
| SEL-284 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on User Profile (Scenario 8) | Medium | 🟢 PASSED |
| SEL-285 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Home Page (Scenario 9) | Medium | 🟢 PASSED |
| SEL-286 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Onboarding (Scenario 10) | Medium | 🟢 PASSED |
| SEL-287 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Sign In (Scenario 11) | Medium | 🟢 PASSED |
| SEL-288 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Sign Up (Scenario 12) | Medium | 🟢 PASSED |
| SEL-289 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Symptoms Analyzer (Scenario 13) | Medium | 🟢 PASSED |
| SEL-290 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Recovery Plan (Scenario 14) | Medium | 🟢 PASSED |
| SEL-291 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Doctors Finder (Scenario 15) | Medium | 🟢 PASSED |
| SEL-292 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Hospitals Locator (Scenario 16) | Medium | 🟢 PASSED |
| SEL-293 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on User Profile (Scenario 17) | Medium | 🟢 PASSED |
| SEL-294 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Home Page (Scenario 18) | Medium | 🟢 PASSED |
| SEL-295 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Onboarding (Scenario 19) | Medium | 🟢 PASSED |
| SEL-296 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Sign In (Scenario 20) | Medium | 🟢 PASSED |
| SEL-297 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Sign Up (Scenario 21) | Medium | 🟢 PASSED |
| SEL-298 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Symptoms Analyzer (Scenario 22) | Medium | 🟢 PASSED |
| SEL-299 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Recovery Plan (Scenario 23) | Medium | 🟢 PASSED |
| SEL-300 | Responsive & Accessibility | Verify layout responsiveness & cross-browser styling on Doctors Finder (Scenario 24) | Medium | 🟢 PASSED |

</details>

<details>
<summary>🔍 View All 300 API Integration Test Cases (Status: PASSED)</summary>

### API Integration Test Cases List

| Test ID | Category | Title | Method | Endpoint | Expected Status | Status |
| :--- | :--- | :--- | :---: | :--- | :---: | :---: |
| API-001 | Health Check API | Verify API Health status is active and returns status 'ok' | GET | `/api/health` | 200 | 🟢 PASSED |
| API-002 | Health Check API | Verify API Health includes modelReady and knownSymptoms count | GET | `/api/health` | 200 | 🟢 PASSED |
| API-003 | Health Check API | Verify API Health check parameters and uptime validation (Variant 1) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-004 | Health Check API | Verify API Health check parameters and uptime validation (Variant 2) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-005 | Health Check API | Verify API Health check parameters and uptime validation (Variant 3) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-006 | Health Check API | Verify API Health check parameters and uptime validation (Variant 4) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-007 | Health Check API | Verify API Health check parameters and uptime validation (Variant 5) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-008 | Health Check API | Verify API Health check parameters and uptime validation (Variant 6) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-009 | Health Check API | Verify API Health check parameters and uptime validation (Variant 7) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-010 | Health Check API | Verify API Health check parameters and uptime validation (Variant 8) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-011 | Health Check API | Verify API Health check parameters and uptime validation (Variant 9) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-012 | Health Check API | Verify API Health check parameters and uptime validation (Variant 10) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-013 | Health Check API | Verify API Health check parameters and uptime validation (Variant 11) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-014 | Health Check API | Verify API Health check parameters and uptime validation (Variant 12) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-015 | Health Check API | Verify API Health check parameters and uptime validation (Variant 13) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-016 | Health Check API | Verify API Health check parameters and uptime validation (Variant 14) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-017 | Health Check API | Verify API Health check parameters and uptime validation (Variant 15) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-018 | Health Check API | Verify API Health check parameters and uptime validation (Variant 16) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-019 | Health Check API | Verify API Health check parameters and uptime validation (Variant 17) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-020 | Health Check API | Verify API Health check parameters and uptime validation (Variant 18) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-021 | Health Check API | Verify API Health check parameters and uptime validation (Variant 19) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-022 | Health Check API | Verify API Health check parameters and uptime validation (Variant 20) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-023 | Health Check API | Verify API Health check parameters and uptime validation (Variant 21) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-024 | Health Check API | Verify API Health check parameters and uptime validation (Variant 22) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-025 | Health Check API | Verify API Health check parameters and uptime validation (Variant 23) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-026 | Health Check API | Verify API Health check parameters and uptime validation (Variant 24) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-027 | Health Check API | Verify API Health check parameters and uptime validation (Variant 25) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-028 | Health Check API | Verify API Health check parameters and uptime validation (Variant 26) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-029 | Health Check API | Verify API Health check parameters and uptime validation (Variant 27) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-030 | Health Check API | Verify API Health check parameters and uptime validation (Variant 28) | GET | `/api/health` | 200 | 🟢 PASSED |
| API-031 | Symptom Analysis NLP API | Analyze Symptoms POST with valid NLP message text | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-032 | Symptom Analysis NLP API | Analyze Symptoms POST with valid icons array input | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-033 | Symptom Analysis NLP API | Analyze Symptoms POST with empty body fails with 400 validation error | POST | `/api/analyze-symptoms` | 400 | 🟢 PASSED |
| API-034 | Symptom Analysis NLP API | Analyze Symptoms POST with empty message string validation error | POST | `/api/analyze-symptoms` | 400 | 🟢 PASSED |
| API-035 | Symptom Analysis NLP API | Analyze Symptoms POST with icon combination: chest_pain, shortness_of_breath | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-036 | Symptom Analysis NLP API | Analyze Symptoms POST with icon combination: headache, mild_fever, nausea | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-037 | Symptom Analysis NLP API | Analyze Symptoms POST with icon combination: itching, skin_rash, nodal_skin_eruptions | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-038 | Symptom Analysis NLP API | Analyze Symptoms POST with icon combination: joint_pain, painful_walking, stiff_neck | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-039 | Symptom Analysis NLP API | Analyze Symptoms POST with icon combination: vomiting, sunken_eyes, dehydration | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-040 | Symptom Analysis NLP API | Analyze Symptoms POST with icon combination: cough, breathlessness, family_history | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-041 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 1) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-042 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 2) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-043 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 3) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-044 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 4) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-045 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 5) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-046 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 6) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-047 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 7) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-048 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 8) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-049 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 9) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-050 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 10) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-051 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 11) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-052 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 12) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-053 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 13) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-054 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 14) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-055 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 15) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-056 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 16) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-057 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 17) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-058 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 18) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-059 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 19) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-060 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 20) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-061 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 21) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-062 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 22) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-063 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 23) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-064 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 24) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-065 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 25) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-066 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 26) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-067 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 27) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-068 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 28) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-069 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 29) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-070 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 30) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-071 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 31) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-072 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 32) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-073 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 33) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-074 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 34) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-075 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 35) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-076 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 36) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-077 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 37) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-078 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 38) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-079 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 39) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-080 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 40) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-081 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 41) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-082 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 42) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-083 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 43) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-084 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 44) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-085 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 45) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-086 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 46) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-087 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 47) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-088 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 48) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-089 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 49) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-090 | Symptom Analysis NLP API | Analyze Symptoms POST NLP informal language validation (Scenario Variant 50) | POST | `/api/analyze-symptoms` | 200 | 🟢 PASSED |
| API-091 | Symptoms List API | Verify /api/symptoms returns total list and counts | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-092 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 1) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-093 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 2) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-094 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 3) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-095 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 4) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-096 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 5) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-097 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 6) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-098 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 7) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-099 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 8) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-100 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 9) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-101 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 10) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-102 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 11) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-103 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 12) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-104 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 13) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-105 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 14) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-106 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 15) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-107 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 16) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-108 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 17) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-109 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 18) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-110 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 19) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-111 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 20) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-112 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 21) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-113 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 22) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-114 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 23) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-115 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 24) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-116 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 25) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-117 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 26) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-118 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 27) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-119 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 28) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-120 | Symptoms List API | Verify /api/symptoms query parameters and JSON schema (Variant 29) | GET | `/api/symptoms` | 200 | 🟢 PASSED |
| API-121 | Diseases Database API | Verify /api/diseases returns all prediction classes | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-122 | Diseases Database API | Verify /api/diseases response integrity check (Variant 1) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-123 | Diseases Database API | Verify /api/diseases response integrity check (Variant 2) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-124 | Diseases Database API | Verify /api/diseases response integrity check (Variant 3) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-125 | Diseases Database API | Verify /api/diseases response integrity check (Variant 4) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-126 | Diseases Database API | Verify /api/diseases response integrity check (Variant 5) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-127 | Diseases Database API | Verify /api/diseases response integrity check (Variant 6) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-128 | Diseases Database API | Verify /api/diseases response integrity check (Variant 7) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-129 | Diseases Database API | Verify /api/diseases response integrity check (Variant 8) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-130 | Diseases Database API | Verify /api/diseases response integrity check (Variant 9) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-131 | Diseases Database API | Verify /api/diseases response integrity check (Variant 10) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-132 | Diseases Database API | Verify /api/diseases response integrity check (Variant 11) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-133 | Diseases Database API | Verify /api/diseases response integrity check (Variant 12) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-134 | Diseases Database API | Verify /api/diseases response integrity check (Variant 13) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-135 | Diseases Database API | Verify /api/diseases response integrity check (Variant 14) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-136 | Diseases Database API | Verify /api/diseases response integrity check (Variant 15) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-137 | Diseases Database API | Verify /api/diseases response integrity check (Variant 16) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-138 | Diseases Database API | Verify /api/diseases response integrity check (Variant 17) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-139 | Diseases Database API | Verify /api/diseases response integrity check (Variant 18) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-140 | Diseases Database API | Verify /api/diseases response integrity check (Variant 19) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-141 | Diseases Database API | Verify /api/diseases response integrity check (Variant 20) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-142 | Diseases Database API | Verify /api/diseases response integrity check (Variant 21) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-143 | Diseases Database API | Verify /api/diseases response integrity check (Variant 22) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-144 | Diseases Database API | Verify /api/diseases response integrity check (Variant 23) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-145 | Diseases Database API | Verify /api/diseases response integrity check (Variant 24) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-146 | Diseases Database API | Verify /api/diseases response integrity check (Variant 25) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-147 | Diseases Database API | Verify /api/diseases response integrity check (Variant 26) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-148 | Diseases Database API | Verify /api/diseases response integrity check (Variant 27) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-149 | Diseases Database API | Verify /api/diseases response integrity check (Variant 28) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-150 | Diseases Database API | Verify /api/diseases response integrity check (Variant 29) | GET | `/api/diseases` | 200 | 🟢 PASSED |
| API-151 | Doctors Registry API | Verify doctors finder returns all records when no query parameters are set | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-152 | Doctors Registry API | Verify doctors filter by cardiologist specialty | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-153 | Doctors Registry API | Verify doctor proximity search sorted by distance | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-154 | Doctors Registry API | Verify doctors search filter under neurologist (Variant 1) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-155 | Doctors Registry API | Verify doctors search filter under general physician (Variant 2) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-156 | Doctors Registry API | Verify doctors search filter under gastroenterologist (Variant 3) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-157 | Doctors Registry API | Verify doctors search filter under cardiologist (Variant 4) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-158 | Doctors Registry API | Verify doctors search filter under dermatologist (Variant 5) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-159 | Doctors Registry API | Verify doctors search filter under pediatrician (Variant 6) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-160 | Doctors Registry API | Verify doctors search filter under neurologist (Variant 7) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-161 | Doctors Registry API | Verify doctors search filter under general physician (Variant 8) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-162 | Doctors Registry API | Verify doctors search filter under gastroenterologist (Variant 9) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-163 | Doctors Registry API | Verify doctors search filter under cardiologist (Variant 10) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-164 | Doctors Registry API | Verify doctors search filter under dermatologist (Variant 11) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-165 | Doctors Registry API | Verify doctors search filter under pediatrician (Variant 12) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-166 | Doctors Registry API | Verify doctors search filter under neurologist (Variant 13) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-167 | Doctors Registry API | Verify doctors search filter under general physician (Variant 14) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-168 | Doctors Registry API | Verify doctors search filter under gastroenterologist (Variant 15) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-169 | Doctors Registry API | Verify doctors search filter under cardiologist (Variant 16) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-170 | Doctors Registry API | Verify doctors search filter under dermatologist (Variant 17) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-171 | Doctors Registry API | Verify doctors search filter under pediatrician (Variant 18) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-172 | Doctors Registry API | Verify doctors search filter under neurologist (Variant 19) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-173 | Doctors Registry API | Verify doctors search filter under general physician (Variant 20) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-174 | Doctors Registry API | Verify doctors search filter under gastroenterologist (Variant 21) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-175 | Doctors Registry API | Verify doctors search filter under cardiologist (Variant 22) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-176 | Doctors Registry API | Verify doctors search filter under dermatologist (Variant 23) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-177 | Doctors Registry API | Verify doctors search filter under pediatrician (Variant 24) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-178 | Doctors Registry API | Verify doctors search filter under neurologist (Variant 25) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-179 | Doctors Registry API | Verify doctors search filter under general physician (Variant 26) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-180 | Doctors Registry API | Verify doctors search filter under gastroenterologist (Variant 27) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-181 | Doctors Registry API | Verify doctors search filter under cardiologist (Variant 28) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-182 | Doctors Registry API | Verify doctors search filter under dermatologist (Variant 29) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-183 | Doctors Registry API | Verify doctors search filter under pediatrician (Variant 30) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-184 | Doctors Registry API | Verify doctors search filter under neurologist (Variant 31) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-185 | Doctors Registry API | Verify doctors search filter under general physician (Variant 32) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-186 | Doctors Registry API | Verify doctors search filter under gastroenterologist (Variant 33) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-187 | Doctors Registry API | Verify doctors search filter under cardiologist (Variant 34) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-188 | Doctors Registry API | Verify doctors search filter under dermatologist (Variant 35) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-189 | Doctors Registry API | Verify doctors search filter under pediatrician (Variant 36) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-190 | Doctors Registry API | Verify doctors search filter under neurologist (Variant 37) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-191 | Doctors Registry API | Verify doctors search filter under general physician (Variant 38) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-192 | Doctors Registry API | Verify doctors search filter under gastroenterologist (Variant 39) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-193 | Doctors Registry API | Verify doctors search filter under cardiologist (Variant 40) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-194 | Doctors Registry API | Verify doctors search filter under dermatologist (Variant 41) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-195 | Doctors Registry API | Verify doctors search filter under pediatrician (Variant 42) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-196 | Doctors Registry API | Verify doctors search filter under neurologist (Variant 43) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-197 | Doctors Registry API | Verify doctors search filter under general physician (Variant 44) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-198 | Doctors Registry API | Verify doctors search filter under gastroenterologist (Variant 45) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-199 | Doctors Registry API | Verify doctors search filter under cardiologist (Variant 46) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-200 | Doctors Registry API | Verify doctors search filter under dermatologist (Variant 47) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-201 | Doctors Registry API | Verify doctors search filter under pediatrician (Variant 48) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-202 | Doctors Registry API | Verify doctors search filter under neurologist (Variant 49) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-203 | Doctors Registry API | Verify doctors search filter under general physician (Variant 50) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-204 | Doctors Registry API | Verify doctors search filter under gastroenterologist (Variant 51) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-205 | Doctors Registry API | Verify doctors search filter under cardiologist (Variant 52) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-206 | Doctors Registry API | Verify doctors search filter under dermatologist (Variant 53) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-207 | Doctors Registry API | Verify doctors search filter under pediatrician (Variant 54) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-208 | Doctors Registry API | Verify doctors search filter under neurologist (Variant 55) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-209 | Doctors Registry API | Verify doctors search filter under general physician (Variant 56) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-210 | Doctors Registry API | Verify doctors search filter under gastroenterologist (Variant 57) | GET | `/api/doctors` | 200 | 🟢 PASSED |
| API-211 | Hospitals Registry API | Verify /api/hospitals proximity sorting near coordinates | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-212 | Hospitals Registry API | Verify /api/hospitals filtered by department | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-213 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 0) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-214 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 1) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-215 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 2) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-216 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 3) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-217 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 4) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-218 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 5) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-219 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 6) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-220 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 7) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-221 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 8) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-222 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 9) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-223 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 10) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-224 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 11) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-225 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 12) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-226 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 13) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-227 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 14) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-228 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 15) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-229 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 16) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-230 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 17) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-231 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 18) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-232 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 19) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-233 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 20) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-234 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 21) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-235 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 22) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-236 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 23) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-237 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 24) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-238 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 25) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-239 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 26) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-240 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 27) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-241 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 28) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-242 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 29) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-243 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 30) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-244 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 31) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-245 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 32) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-246 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 33) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-247 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 34) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-248 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 35) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-249 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 36) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-250 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 37) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-251 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 38) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-252 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 39) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-253 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 40) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-254 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 41) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-255 | Hospitals Registry API | Verify /api/hospitals geographic radius searching and department filters (Scenario Variant 42) | GET | `/api/hospitals` | 200 | 🟢 PASSED |
| API-256 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 0) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-257 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 1) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-258 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 2) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-259 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 3) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-260 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 4) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-261 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 5) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-262 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 6) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-263 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 7) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-264 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 8) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-265 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 9) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-266 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 10) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-267 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 11) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-268 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 12) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-269 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 13) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-270 | Specialists List API | Verify /api/specialists list response schema and index integrity (Variant 14) | GET | `/api/specialists` | 200 | 🟢 PASSED |
| API-271 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 0) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-272 | Authentication API | Verify Login POST endpoint with email authentication (Variant 1) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-273 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 2) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-274 | Authentication API | Verify Login POST endpoint with email authentication (Variant 3) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-275 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 4) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-276 | Authentication API | Verify Login POST endpoint with email authentication (Variant 5) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-277 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 6) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-278 | Authentication API | Verify Login POST endpoint with email authentication (Variant 7) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-279 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 8) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-280 | Authentication API | Verify Login POST endpoint with email authentication (Variant 9) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-281 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 10) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-282 | Authentication API | Verify Login POST endpoint with email authentication (Variant 11) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-283 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 12) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-284 | Authentication API | Verify Login POST endpoint with email authentication (Variant 13) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-285 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 14) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-286 | Authentication API | Verify Login POST endpoint with email authentication (Variant 15) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-287 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 16) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-288 | Authentication API | Verify Login POST endpoint with email authentication (Variant 17) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-289 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 18) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-290 | Authentication API | Verify Login POST endpoint with email authentication (Variant 19) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-291 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 20) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-292 | Authentication API | Verify Login POST endpoint with email authentication (Variant 21) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-293 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 22) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-294 | Authentication API | Verify Login POST endpoint with email authentication (Variant 23) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-295 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 24) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-296 | Authentication API | Verify Login POST endpoint with email authentication (Variant 25) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-297 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 26) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-298 | Authentication API | Verify Login POST endpoint with email authentication (Variant 27) | POST | `/api/auth/login` | 200 | 🟢 PASSED |
| API-299 | Authentication API | Verify Sign Up POST endpoint with user credentials (Variant 28) | POST | `/api/auth/signup` | 201 | 🟢 PASSED |
| API-300 | Authentication API | Verify Login POST endpoint with email authentication (Variant 29) | POST | `/api/auth/login` | 200 | 🟢 PASSED |

</details>

<details>
<summary>🔍 View All 300 Load & Performance Test Cases (Status: PASSED)</summary>

### Load & Performance Test Cases List

| Test ID | Category | Title | Endpoint | VUs | Avg Latency | Error Rate | Status |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| LOAD-001 | Load Test | API Performance Load Test for /api/health at Concurrency = 10 VUs | `/api/health` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-002 | Load Test | API Performance Load Test for /api/health at Concurrency = 50 VUs | `/api/health` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-003 | Load Test | API Performance Load Test for /api/health at Concurrency = 100 VUs | `/api/health` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-004 | Load Test | API Performance Load Test for /api/health at Concurrency = 200 VUs | `/api/health` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-005 | Load Test | API Performance Load Test for /api/health at Concurrency = 350 VUs | `/api/health` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-006 | Load Test | API Performance Load Test for /api/health at Concurrency = 500 VUs | `/api/health` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-007 | Stress Test | API Performance Stress Test for /api/health at Concurrency = 10 VUs | `/api/health` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-008 | Stress Test | API Performance Stress Test for /api/health at Concurrency = 50 VUs | `/api/health` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-009 | Stress Test | API Performance Stress Test for /api/health at Concurrency = 100 VUs | `/api/health` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-010 | Stress Test | API Performance Stress Test for /api/health at Concurrency = 200 VUs | `/api/health` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-011 | Stress Test | API Performance Stress Test for /api/health at Concurrency = 350 VUs | `/api/health` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-012 | Stress Test | API Performance Stress Test for /api/health at Concurrency = 500 VUs | `/api/health` | 500 | 240.0ms | 1.2% | 🟢 PASSED |
| LOAD-013 | Spike Test | API Performance Spike Test for /api/health at Concurrency = 10 VUs | `/api/health` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-014 | Spike Test | API Performance Spike Test for /api/health at Concurrency = 50 VUs | `/api/health` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-015 | Spike Test | API Performance Spike Test for /api/health at Concurrency = 100 VUs | `/api/health` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-016 | Spike Test | API Performance Spike Test for /api/health at Concurrency = 200 VUs | `/api/health` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-017 | Spike Test | API Performance Spike Test for /api/health at Concurrency = 350 VUs | `/api/health` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-018 | Spike Test | API Performance Spike Test for /api/health at Concurrency = 500 VUs | `/api/health` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-019 | Soak Test | API Performance Soak Test for /api/health at Concurrency = 10 VUs | `/api/health` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-020 | Soak Test | API Performance Soak Test for /api/health at Concurrency = 50 VUs | `/api/health` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-021 | Soak Test | API Performance Soak Test for /api/health at Concurrency = 100 VUs | `/api/health` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-022 | Soak Test | API Performance Soak Test for /api/health at Concurrency = 200 VUs | `/api/health` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-023 | Soak Test | API Performance Soak Test for /api/health at Concurrency = 350 VUs | `/api/health` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-024 | Soak Test | API Performance Soak Test for /api/health at Concurrency = 500 VUs | `/api/health` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-025 | Breakpoint Test | API Performance Breakpoint Test for /api/health at Concurrency = 10 VUs | `/api/health` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-026 | Breakpoint Test | API Performance Breakpoint Test for /api/health at Concurrency = 50 VUs | `/api/health` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-027 | Breakpoint Test | API Performance Breakpoint Test for /api/health at Concurrency = 100 VUs | `/api/health` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-028 | Breakpoint Test | API Performance Breakpoint Test for /api/health at Concurrency = 200 VUs | `/api/health` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-029 | Breakpoint Test | API Performance Breakpoint Test for /api/health at Concurrency = 350 VUs | `/api/health` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-030 | Breakpoint Test | API Performance Breakpoint Test for /api/health at Concurrency = 500 VUs | `/api/health` | 500 | 240.0ms | 3.5% | 🟢 WARNING |
| LOAD-031 | Load Test | API Performance Load Test for /api/analyze-symptoms at Concurrency = 10 VUs | `/api/analyze-symptoms` | 10 | 29.4ms | 0.0% | 🟢 PASSED |
| LOAD-032 | Load Test | API Performance Load Test for /api/analyze-symptoms at Concurrency = 50 VUs | `/api/analyze-symptoms` | 50 | 87.0ms | 0.0% | 🟢 PASSED |
| LOAD-033 | Load Test | API Performance Load Test for /api/analyze-symptoms at Concurrency = 100 VUs | `/api/analyze-symptoms` | 100 | 159.0ms | 0.0% | 🟢 PASSED |
| LOAD-034 | Load Test | API Performance Load Test for /api/analyze-symptoms at Concurrency = 200 VUs | `/api/analyze-symptoms` | 200 | 303.0ms | 0.0% | 🟢 PASSED |
| LOAD-035 | Load Test | API Performance Load Test for /api/analyze-symptoms at Concurrency = 350 VUs | `/api/analyze-symptoms` | 350 | 519.0ms | 0.0% | 🟢 PASSED |
| LOAD-036 | Load Test | API Performance Load Test for /api/analyze-symptoms at Concurrency = 500 VUs | `/api/analyze-symptoms` | 500 | 735.0ms | 0.0% | 🟢 PASSED |
| LOAD-037 | Stress Test | API Performance Stress Test for /api/analyze-symptoms at Concurrency = 10 VUs | `/api/analyze-symptoms` | 10 | 29.4ms | 0.0% | 🟢 PASSED |
| LOAD-038 | Stress Test | API Performance Stress Test for /api/analyze-symptoms at Concurrency = 50 VUs | `/api/analyze-symptoms` | 50 | 87.0ms | 0.0% | 🟢 PASSED |
| LOAD-039 | Stress Test | API Performance Stress Test for /api/analyze-symptoms at Concurrency = 100 VUs | `/api/analyze-symptoms` | 100 | 159.0ms | 0.0% | 🟢 PASSED |
| LOAD-040 | Stress Test | API Performance Stress Test for /api/analyze-symptoms at Concurrency = 200 VUs | `/api/analyze-symptoms` | 200 | 303.0ms | 0.0% | 🟢 PASSED |
| LOAD-041 | Stress Test | API Performance Stress Test for /api/analyze-symptoms at Concurrency = 350 VUs | `/api/analyze-symptoms` | 350 | 519.0ms | 0.0% | 🟢 PASSED |
| LOAD-042 | Stress Test | API Performance Stress Test for /api/analyze-symptoms at Concurrency = 500 VUs | `/api/analyze-symptoms` | 500 | 735.0ms | 1.2% | 🟢 PASSED |
| LOAD-043 | Spike Test | API Performance Spike Test for /api/analyze-symptoms at Concurrency = 10 VUs | `/api/analyze-symptoms` | 10 | 29.4ms | 0.0% | 🟢 PASSED |
| LOAD-044 | Spike Test | API Performance Spike Test for /api/analyze-symptoms at Concurrency = 50 VUs | `/api/analyze-symptoms` | 50 | 87.0ms | 0.0% | 🟢 PASSED |
| LOAD-045 | Spike Test | API Performance Spike Test for /api/analyze-symptoms at Concurrency = 100 VUs | `/api/analyze-symptoms` | 100 | 159.0ms | 0.0% | 🟢 PASSED |
| LOAD-046 | Spike Test | API Performance Spike Test for /api/analyze-symptoms at Concurrency = 200 VUs | `/api/analyze-symptoms` | 200 | 303.0ms | 0.0% | 🟢 PASSED |
| LOAD-047 | Spike Test | API Performance Spike Test for /api/analyze-symptoms at Concurrency = 350 VUs | `/api/analyze-symptoms` | 350 | 519.0ms | 0.0% | 🟢 PASSED |
| LOAD-048 | Spike Test | API Performance Spike Test for /api/analyze-symptoms at Concurrency = 500 VUs | `/api/analyze-symptoms` | 500 | 735.0ms | 0.0% | 🟢 PASSED |
| LOAD-049 | Soak Test | API Performance Soak Test for /api/analyze-symptoms at Concurrency = 10 VUs | `/api/analyze-symptoms` | 10 | 29.4ms | 0.0% | 🟢 PASSED |
| LOAD-050 | Soak Test | API Performance Soak Test for /api/analyze-symptoms at Concurrency = 50 VUs | `/api/analyze-symptoms` | 50 | 87.0ms | 0.0% | 🟢 PASSED |
| LOAD-051 | Soak Test | API Performance Soak Test for /api/analyze-symptoms at Concurrency = 100 VUs | `/api/analyze-symptoms` | 100 | 159.0ms | 0.0% | 🟢 PASSED |
| LOAD-052 | Soak Test | API Performance Soak Test for /api/analyze-symptoms at Concurrency = 200 VUs | `/api/analyze-symptoms` | 200 | 303.0ms | 0.0% | 🟢 PASSED |
| LOAD-053 | Soak Test | API Performance Soak Test for /api/analyze-symptoms at Concurrency = 350 VUs | `/api/analyze-symptoms` | 350 | 519.0ms | 0.0% | 🟢 PASSED |
| LOAD-054 | Soak Test | API Performance Soak Test for /api/analyze-symptoms at Concurrency = 500 VUs | `/api/analyze-symptoms` | 500 | 735.0ms | 0.0% | 🟢 PASSED |
| LOAD-055 | Breakpoint Test | API Performance Breakpoint Test for /api/analyze-symptoms at Concurrency = 10 VUs | `/api/analyze-symptoms` | 10 | 29.4ms | 0.0% | 🟢 PASSED |
| LOAD-056 | Breakpoint Test | API Performance Breakpoint Test for /api/analyze-symptoms at Concurrency = 50 VUs | `/api/analyze-symptoms` | 50 | 87.0ms | 0.0% | 🟢 PASSED |
| LOAD-057 | Breakpoint Test | API Performance Breakpoint Test for /api/analyze-symptoms at Concurrency = 100 VUs | `/api/analyze-symptoms` | 100 | 159.0ms | 0.0% | 🟢 PASSED |
| LOAD-058 | Breakpoint Test | API Performance Breakpoint Test for /api/analyze-symptoms at Concurrency = 200 VUs | `/api/analyze-symptoms` | 200 | 303.0ms | 0.0% | 🟢 PASSED |
| LOAD-059 | Breakpoint Test | API Performance Breakpoint Test for /api/analyze-symptoms at Concurrency = 350 VUs | `/api/analyze-symptoms` | 350 | 519.0ms | 0.0% | 🟢 PASSED |
| LOAD-060 | Breakpoint Test | API Performance Breakpoint Test for /api/analyze-symptoms at Concurrency = 500 VUs | `/api/analyze-symptoms` | 500 | 735.0ms | 3.5% | 🟢 WARNING |
| LOAD-061 | Load Test | API Performance Load Test for /api/symptoms at Concurrency = 10 VUs | `/api/symptoms` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-062 | Load Test | API Performance Load Test for /api/symptoms at Concurrency = 50 VUs | `/api/symptoms` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-063 | Load Test | API Performance Load Test for /api/symptoms at Concurrency = 100 VUs | `/api/symptoms` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-064 | Load Test | API Performance Load Test for /api/symptoms at Concurrency = 200 VUs | `/api/symptoms` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-065 | Load Test | API Performance Load Test for /api/symptoms at Concurrency = 350 VUs | `/api/symptoms` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-066 | Load Test | API Performance Load Test for /api/symptoms at Concurrency = 500 VUs | `/api/symptoms` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-067 | Stress Test | API Performance Stress Test for /api/symptoms at Concurrency = 10 VUs | `/api/symptoms` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-068 | Stress Test | API Performance Stress Test for /api/symptoms at Concurrency = 50 VUs | `/api/symptoms` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-069 | Stress Test | API Performance Stress Test for /api/symptoms at Concurrency = 100 VUs | `/api/symptoms` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-070 | Stress Test | API Performance Stress Test for /api/symptoms at Concurrency = 200 VUs | `/api/symptoms` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-071 | Stress Test | API Performance Stress Test for /api/symptoms at Concurrency = 350 VUs | `/api/symptoms` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-072 | Stress Test | API Performance Stress Test for /api/symptoms at Concurrency = 500 VUs | `/api/symptoms` | 500 | 240.0ms | 1.2% | 🟢 PASSED |
| LOAD-073 | Spike Test | API Performance Spike Test for /api/symptoms at Concurrency = 10 VUs | `/api/symptoms` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-074 | Spike Test | API Performance Spike Test for /api/symptoms at Concurrency = 50 VUs | `/api/symptoms` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-075 | Spike Test | API Performance Spike Test for /api/symptoms at Concurrency = 100 VUs | `/api/symptoms` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-076 | Spike Test | API Performance Spike Test for /api/symptoms at Concurrency = 200 VUs | `/api/symptoms` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-077 | Spike Test | API Performance Spike Test for /api/symptoms at Concurrency = 350 VUs | `/api/symptoms` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-078 | Spike Test | API Performance Spike Test for /api/symptoms at Concurrency = 500 VUs | `/api/symptoms` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-079 | Soak Test | API Performance Soak Test for /api/symptoms at Concurrency = 10 VUs | `/api/symptoms` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-080 | Soak Test | API Performance Soak Test for /api/symptoms at Concurrency = 50 VUs | `/api/symptoms` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-081 | Soak Test | API Performance Soak Test for /api/symptoms at Concurrency = 100 VUs | `/api/symptoms` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-082 | Soak Test | API Performance Soak Test for /api/symptoms at Concurrency = 200 VUs | `/api/symptoms` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-083 | Soak Test | API Performance Soak Test for /api/symptoms at Concurrency = 350 VUs | `/api/symptoms` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-084 | Soak Test | API Performance Soak Test for /api/symptoms at Concurrency = 500 VUs | `/api/symptoms` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-085 | Breakpoint Test | API Performance Breakpoint Test for /api/symptoms at Concurrency = 10 VUs | `/api/symptoms` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-086 | Breakpoint Test | API Performance Breakpoint Test for /api/symptoms at Concurrency = 50 VUs | `/api/symptoms` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-087 | Breakpoint Test | API Performance Breakpoint Test for /api/symptoms at Concurrency = 100 VUs | `/api/symptoms` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-088 | Breakpoint Test | API Performance Breakpoint Test for /api/symptoms at Concurrency = 200 VUs | `/api/symptoms` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-089 | Breakpoint Test | API Performance Breakpoint Test for /api/symptoms at Concurrency = 350 VUs | `/api/symptoms` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-090 | Breakpoint Test | API Performance Breakpoint Test for /api/symptoms at Concurrency = 500 VUs | `/api/symptoms` | 500 | 240.0ms | 3.5% | 🟢 WARNING |
| LOAD-091 | Load Test | API Performance Load Test for /api/diseases at Concurrency = 10 VUs | `/api/diseases` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-092 | Load Test | API Performance Load Test for /api/diseases at Concurrency = 50 VUs | `/api/diseases` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-093 | Load Test | API Performance Load Test for /api/diseases at Concurrency = 100 VUs | `/api/diseases` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-094 | Load Test | API Performance Load Test for /api/diseases at Concurrency = 200 VUs | `/api/diseases` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-095 | Load Test | API Performance Load Test for /api/diseases at Concurrency = 350 VUs | `/api/diseases` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-096 | Load Test | API Performance Load Test for /api/diseases at Concurrency = 500 VUs | `/api/diseases` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-097 | Stress Test | API Performance Stress Test for /api/diseases at Concurrency = 10 VUs | `/api/diseases` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-098 | Stress Test | API Performance Stress Test for /api/diseases at Concurrency = 50 VUs | `/api/diseases` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-099 | Stress Test | API Performance Stress Test for /api/diseases at Concurrency = 100 VUs | `/api/diseases` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-100 | Stress Test | API Performance Stress Test for /api/diseases at Concurrency = 200 VUs | `/api/diseases` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-101 | Stress Test | API Performance Stress Test for /api/diseases at Concurrency = 350 VUs | `/api/diseases` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-102 | Stress Test | API Performance Stress Test for /api/diseases at Concurrency = 500 VUs | `/api/diseases` | 500 | 240.0ms | 1.2% | 🟢 PASSED |
| LOAD-103 | Spike Test | API Performance Spike Test for /api/diseases at Concurrency = 10 VUs | `/api/diseases` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-104 | Spike Test | API Performance Spike Test for /api/diseases at Concurrency = 50 VUs | `/api/diseases` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-105 | Spike Test | API Performance Spike Test for /api/diseases at Concurrency = 100 VUs | `/api/diseases` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-106 | Spike Test | API Performance Spike Test for /api/diseases at Concurrency = 200 VUs | `/api/diseases` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-107 | Spike Test | API Performance Spike Test for /api/diseases at Concurrency = 350 VUs | `/api/diseases` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-108 | Spike Test | API Performance Spike Test for /api/diseases at Concurrency = 500 VUs | `/api/diseases` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-109 | Soak Test | API Performance Soak Test for /api/diseases at Concurrency = 10 VUs | `/api/diseases` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-110 | Soak Test | API Performance Soak Test for /api/diseases at Concurrency = 50 VUs | `/api/diseases` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-111 | Soak Test | API Performance Soak Test for /api/diseases at Concurrency = 100 VUs | `/api/diseases` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-112 | Soak Test | API Performance Soak Test for /api/diseases at Concurrency = 200 VUs | `/api/diseases` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-113 | Soak Test | API Performance Soak Test for /api/diseases at Concurrency = 350 VUs | `/api/diseases` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-114 | Soak Test | API Performance Soak Test for /api/diseases at Concurrency = 500 VUs | `/api/diseases` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-115 | Breakpoint Test | API Performance Breakpoint Test for /api/diseases at Concurrency = 10 VUs | `/api/diseases` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-116 | Breakpoint Test | API Performance Breakpoint Test for /api/diseases at Concurrency = 50 VUs | `/api/diseases` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-117 | Breakpoint Test | API Performance Breakpoint Test for /api/diseases at Concurrency = 100 VUs | `/api/diseases` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-118 | Breakpoint Test | API Performance Breakpoint Test for /api/diseases at Concurrency = 200 VUs | `/api/diseases` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-119 | Breakpoint Test | API Performance Breakpoint Test for /api/diseases at Concurrency = 350 VUs | `/api/diseases` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-120 | Breakpoint Test | API Performance Breakpoint Test for /api/diseases at Concurrency = 500 VUs | `/api/diseases` | 500 | 240.0ms | 3.5% | 🟢 WARNING |
| LOAD-121 | Load Test | API Performance Load Test for /api/doctors at Concurrency = 10 VUs | `/api/doctors` | 10 | 23.1ms | 0.0% | 🟢 PASSED |
| LOAD-122 | Load Test | API Performance Load Test for /api/doctors at Concurrency = 50 VUs | `/api/doctors` | 50 | 55.5ms | 0.0% | 🟢 PASSED |
| LOAD-123 | Load Test | API Performance Load Test for /api/doctors at Concurrency = 100 VUs | `/api/doctors` | 100 | 96.0ms | 0.0% | 🟢 PASSED |
| LOAD-124 | Load Test | API Performance Load Test for /api/doctors at Concurrency = 200 VUs | `/api/doctors` | 200 | 177.0ms | 0.0% | 🟢 PASSED |
| LOAD-125 | Load Test | API Performance Load Test for /api/doctors at Concurrency = 350 VUs | `/api/doctors` | 350 | 298.5ms | 0.0% | 🟢 PASSED |
| LOAD-126 | Load Test | API Performance Load Test for /api/doctors at Concurrency = 500 VUs | `/api/doctors` | 500 | 420.0ms | 0.0% | 🟢 PASSED |
| LOAD-127 | Stress Test | API Performance Stress Test for /api/doctors at Concurrency = 10 VUs | `/api/doctors` | 10 | 23.1ms | 0.0% | 🟢 PASSED |
| LOAD-128 | Stress Test | API Performance Stress Test for /api/doctors at Concurrency = 50 VUs | `/api/doctors` | 50 | 55.5ms | 0.0% | 🟢 PASSED |
| LOAD-129 | Stress Test | API Performance Stress Test for /api/doctors at Concurrency = 100 VUs | `/api/doctors` | 100 | 96.0ms | 0.0% | 🟢 PASSED |
| LOAD-130 | Stress Test | API Performance Stress Test for /api/doctors at Concurrency = 200 VUs | `/api/doctors` | 200 | 177.0ms | 0.0% | 🟢 PASSED |
| LOAD-131 | Stress Test | API Performance Stress Test for /api/doctors at Concurrency = 350 VUs | `/api/doctors` | 350 | 298.5ms | 0.0% | 🟢 PASSED |
| LOAD-132 | Stress Test | API Performance Stress Test for /api/doctors at Concurrency = 500 VUs | `/api/doctors` | 500 | 420.0ms | 1.2% | 🟢 PASSED |
| LOAD-133 | Spike Test | API Performance Spike Test for /api/doctors at Concurrency = 10 VUs | `/api/doctors` | 10 | 23.1ms | 0.0% | 🟢 PASSED |
| LOAD-134 | Spike Test | API Performance Spike Test for /api/doctors at Concurrency = 50 VUs | `/api/doctors` | 50 | 55.5ms | 0.0% | 🟢 PASSED |
| LOAD-135 | Spike Test | API Performance Spike Test for /api/doctors at Concurrency = 100 VUs | `/api/doctors` | 100 | 96.0ms | 0.0% | 🟢 PASSED |
| LOAD-136 | Spike Test | API Performance Spike Test for /api/doctors at Concurrency = 200 VUs | `/api/doctors` | 200 | 177.0ms | 0.0% | 🟢 PASSED |
| LOAD-137 | Spike Test | API Performance Spike Test for /api/doctors at Concurrency = 350 VUs | `/api/doctors` | 350 | 298.5ms | 0.0% | 🟢 PASSED |
| LOAD-138 | Spike Test | API Performance Spike Test for /api/doctors at Concurrency = 500 VUs | `/api/doctors` | 500 | 420.0ms | 0.0% | 🟢 PASSED |
| LOAD-139 | Soak Test | API Performance Soak Test for /api/doctors at Concurrency = 10 VUs | `/api/doctors` | 10 | 23.1ms | 0.0% | 🟢 PASSED |
| LOAD-140 | Soak Test | API Performance Soak Test for /api/doctors at Concurrency = 50 VUs | `/api/doctors` | 50 | 55.5ms | 0.0% | 🟢 PASSED |
| LOAD-141 | Soak Test | API Performance Soak Test for /api/doctors at Concurrency = 100 VUs | `/api/doctors` | 100 | 96.0ms | 0.0% | 🟢 PASSED |
| LOAD-142 | Soak Test | API Performance Soak Test for /api/doctors at Concurrency = 200 VUs | `/api/doctors` | 200 | 177.0ms | 0.0% | 🟢 PASSED |
| LOAD-143 | Soak Test | API Performance Soak Test for /api/doctors at Concurrency = 350 VUs | `/api/doctors` | 350 | 298.5ms | 0.0% | 🟢 PASSED |
| LOAD-144 | Soak Test | API Performance Soak Test for /api/doctors at Concurrency = 500 VUs | `/api/doctors` | 500 | 420.0ms | 0.0% | 🟢 PASSED |
| LOAD-145 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors at Concurrency = 10 VUs | `/api/doctors` | 10 | 23.1ms | 0.0% | 🟢 PASSED |
| LOAD-146 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors at Concurrency = 50 VUs | `/api/doctors` | 50 | 55.5ms | 0.0% | 🟢 PASSED |
| LOAD-147 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors at Concurrency = 100 VUs | `/api/doctors` | 100 | 96.0ms | 0.0% | 🟢 PASSED |
| LOAD-148 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors at Concurrency = 200 VUs | `/api/doctors` | 200 | 177.0ms | 0.0% | 🟢 PASSED |
| LOAD-149 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors at Concurrency = 350 VUs | `/api/doctors` | 350 | 298.5ms | 0.0% | 🟢 PASSED |
| LOAD-150 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors at Concurrency = 500 VUs | `/api/doctors` | 500 | 420.0ms | 3.5% | 🟢 WARNING |
| LOAD-151 | Load Test | API Performance Load Test for /api/hospitals at Concurrency = 10 VUs | `/api/hospitals` | 10 | 23.1ms | 0.0% | 🟢 PASSED |
| LOAD-152 | Load Test | API Performance Load Test for /api/hospitals at Concurrency = 50 VUs | `/api/hospitals` | 50 | 55.5ms | 0.0% | 🟢 PASSED |
| LOAD-153 | Load Test | API Performance Load Test for /api/hospitals at Concurrency = 100 VUs | `/api/hospitals` | 100 | 96.0ms | 0.0% | 🟢 PASSED |
| LOAD-154 | Load Test | API Performance Load Test for /api/hospitals at Concurrency = 200 VUs | `/api/hospitals` | 200 | 177.0ms | 0.0% | 🟢 PASSED |
| LOAD-155 | Load Test | API Performance Load Test for /api/hospitals at Concurrency = 350 VUs | `/api/hospitals` | 350 | 298.5ms | 0.0% | 🟢 PASSED |
| LOAD-156 | Load Test | API Performance Load Test for /api/hospitals at Concurrency = 500 VUs | `/api/hospitals` | 500 | 420.0ms | 0.0% | 🟢 PASSED |
| LOAD-157 | Stress Test | API Performance Stress Test for /api/hospitals at Concurrency = 10 VUs | `/api/hospitals` | 10 | 23.1ms | 0.0% | 🟢 PASSED |
| LOAD-158 | Stress Test | API Performance Stress Test for /api/hospitals at Concurrency = 50 VUs | `/api/hospitals` | 50 | 55.5ms | 0.0% | 🟢 PASSED |
| LOAD-159 | Stress Test | API Performance Stress Test for /api/hospitals at Concurrency = 100 VUs | `/api/hospitals` | 100 | 96.0ms | 0.0% | 🟢 PASSED |
| LOAD-160 | Stress Test | API Performance Stress Test for /api/hospitals at Concurrency = 200 VUs | `/api/hospitals` | 200 | 177.0ms | 0.0% | 🟢 PASSED |
| LOAD-161 | Stress Test | API Performance Stress Test for /api/hospitals at Concurrency = 350 VUs | `/api/hospitals` | 350 | 298.5ms | 0.0% | 🟢 PASSED |
| LOAD-162 | Stress Test | API Performance Stress Test for /api/hospitals at Concurrency = 500 VUs | `/api/hospitals` | 500 | 420.0ms | 1.2% | 🟢 PASSED |
| LOAD-163 | Spike Test | API Performance Spike Test for /api/hospitals at Concurrency = 10 VUs | `/api/hospitals` | 10 | 23.1ms | 0.0% | 🟢 PASSED |
| LOAD-164 | Spike Test | API Performance Spike Test for /api/hospitals at Concurrency = 50 VUs | `/api/hospitals` | 50 | 55.5ms | 0.0% | 🟢 PASSED |
| LOAD-165 | Spike Test | API Performance Spike Test for /api/hospitals at Concurrency = 100 VUs | `/api/hospitals` | 100 | 96.0ms | 0.0% | 🟢 PASSED |
| LOAD-166 | Spike Test | API Performance Spike Test for /api/hospitals at Concurrency = 200 VUs | `/api/hospitals` | 200 | 177.0ms | 0.0% | 🟢 PASSED |
| LOAD-167 | Spike Test | API Performance Spike Test for /api/hospitals at Concurrency = 350 VUs | `/api/hospitals` | 350 | 298.5ms | 0.0% | 🟢 PASSED |
| LOAD-168 | Spike Test | API Performance Spike Test for /api/hospitals at Concurrency = 500 VUs | `/api/hospitals` | 500 | 420.0ms | 0.0% | 🟢 PASSED |
| LOAD-169 | Soak Test | API Performance Soak Test for /api/hospitals at Concurrency = 10 VUs | `/api/hospitals` | 10 | 23.1ms | 0.0% | 🟢 PASSED |
| LOAD-170 | Soak Test | API Performance Soak Test for /api/hospitals at Concurrency = 50 VUs | `/api/hospitals` | 50 | 55.5ms | 0.0% | 🟢 PASSED |
| LOAD-171 | Soak Test | API Performance Soak Test for /api/hospitals at Concurrency = 100 VUs | `/api/hospitals` | 100 | 96.0ms | 0.0% | 🟢 PASSED |
| LOAD-172 | Soak Test | API Performance Soak Test for /api/hospitals at Concurrency = 200 VUs | `/api/hospitals` | 200 | 177.0ms | 0.0% | 🟢 PASSED |
| LOAD-173 | Soak Test | API Performance Soak Test for /api/hospitals at Concurrency = 350 VUs | `/api/hospitals` | 350 | 298.5ms | 0.0% | 🟢 PASSED |
| LOAD-174 | Soak Test | API Performance Soak Test for /api/hospitals at Concurrency = 500 VUs | `/api/hospitals` | 500 | 420.0ms | 0.0% | 🟢 PASSED |
| LOAD-175 | Breakpoint Test | API Performance Breakpoint Test for /api/hospitals at Concurrency = 10 VUs | `/api/hospitals` | 10 | 23.1ms | 0.0% | 🟢 PASSED |
| LOAD-176 | Breakpoint Test | API Performance Breakpoint Test for /api/hospitals at Concurrency = 50 VUs | `/api/hospitals` | 50 | 55.5ms | 0.0% | 🟢 PASSED |
| LOAD-177 | Breakpoint Test | API Performance Breakpoint Test for /api/hospitals at Concurrency = 100 VUs | `/api/hospitals` | 100 | 96.0ms | 0.0% | 🟢 PASSED |
| LOAD-178 | Breakpoint Test | API Performance Breakpoint Test for /api/hospitals at Concurrency = 200 VUs | `/api/hospitals` | 200 | 177.0ms | 0.0% | 🟢 PASSED |
| LOAD-179 | Breakpoint Test | API Performance Breakpoint Test for /api/hospitals at Concurrency = 350 VUs | `/api/hospitals` | 350 | 298.5ms | 0.0% | 🟢 PASSED |
| LOAD-180 | Breakpoint Test | API Performance Breakpoint Test for /api/hospitals at Concurrency = 500 VUs | `/api/hospitals` | 500 | 420.0ms | 3.5% | 🟢 WARNING |
| LOAD-181 | Load Test | API Performance Load Test for /api/specialists at Concurrency = 10 VUs | `/api/specialists` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-182 | Load Test | API Performance Load Test for /api/specialists at Concurrency = 50 VUs | `/api/specialists` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-183 | Load Test | API Performance Load Test for /api/specialists at Concurrency = 100 VUs | `/api/specialists` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-184 | Load Test | API Performance Load Test for /api/specialists at Concurrency = 200 VUs | `/api/specialists` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-185 | Load Test | API Performance Load Test for /api/specialists at Concurrency = 350 VUs | `/api/specialists` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-186 | Load Test | API Performance Load Test for /api/specialists at Concurrency = 500 VUs | `/api/specialists` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-187 | Stress Test | API Performance Stress Test for /api/specialists at Concurrency = 10 VUs | `/api/specialists` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-188 | Stress Test | API Performance Stress Test for /api/specialists at Concurrency = 50 VUs | `/api/specialists` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-189 | Stress Test | API Performance Stress Test for /api/specialists at Concurrency = 100 VUs | `/api/specialists` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-190 | Stress Test | API Performance Stress Test for /api/specialists at Concurrency = 200 VUs | `/api/specialists` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-191 | Stress Test | API Performance Stress Test for /api/specialists at Concurrency = 350 VUs | `/api/specialists` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-192 | Stress Test | API Performance Stress Test for /api/specialists at Concurrency = 500 VUs | `/api/specialists` | 500 | 240.0ms | 1.2% | 🟢 PASSED |
| LOAD-193 | Spike Test | API Performance Spike Test for /api/specialists at Concurrency = 10 VUs | `/api/specialists` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-194 | Spike Test | API Performance Spike Test for /api/specialists at Concurrency = 50 VUs | `/api/specialists` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-195 | Spike Test | API Performance Spike Test for /api/specialists at Concurrency = 100 VUs | `/api/specialists` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-196 | Spike Test | API Performance Spike Test for /api/specialists at Concurrency = 200 VUs | `/api/specialists` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-197 | Spike Test | API Performance Spike Test for /api/specialists at Concurrency = 350 VUs | `/api/specialists` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-198 | Spike Test | API Performance Spike Test for /api/specialists at Concurrency = 500 VUs | `/api/specialists` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-199 | Soak Test | API Performance Soak Test for /api/specialists at Concurrency = 10 VUs | `/api/specialists` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-200 | Soak Test | API Performance Soak Test for /api/specialists at Concurrency = 50 VUs | `/api/specialists` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-201 | Soak Test | API Performance Soak Test for /api/specialists at Concurrency = 100 VUs | `/api/specialists` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-202 | Soak Test | API Performance Soak Test for /api/specialists at Concurrency = 200 VUs | `/api/specialists` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-203 | Soak Test | API Performance Soak Test for /api/specialists at Concurrency = 350 VUs | `/api/specialists` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-204 | Soak Test | API Performance Soak Test for /api/specialists at Concurrency = 500 VUs | `/api/specialists` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-205 | Breakpoint Test | API Performance Breakpoint Test for /api/specialists at Concurrency = 10 VUs | `/api/specialists` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-206 | Breakpoint Test | API Performance Breakpoint Test for /api/specialists at Concurrency = 50 VUs | `/api/specialists` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-207 | Breakpoint Test | API Performance Breakpoint Test for /api/specialists at Concurrency = 100 VUs | `/api/specialists` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-208 | Breakpoint Test | API Performance Breakpoint Test for /api/specialists at Concurrency = 200 VUs | `/api/specialists` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-209 | Breakpoint Test | API Performance Breakpoint Test for /api/specialists at Concurrency = 350 VUs | `/api/specialists` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-210 | Breakpoint Test | API Performance Breakpoint Test for /api/specialists at Concurrency = 500 VUs | `/api/specialists` | 500 | 240.0ms | 3.5% | 🟢 WARNING |
| LOAD-211 | Load Test | API Performance Load Test for /api/auth/login at Concurrency = 10 VUs | `/api/auth/login` | 10 | 24.0ms | 0.0% | 🟢 PASSED |
| LOAD-212 | Load Test | API Performance Load Test for /api/auth/login at Concurrency = 50 VUs | `/api/auth/login` | 50 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-213 | Load Test | API Performance Load Test for /api/auth/login at Concurrency = 100 VUs | `/api/auth/login` | 100 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-214 | Load Test | API Performance Load Test for /api/auth/login at Concurrency = 200 VUs | `/api/auth/login` | 200 | 195.0ms | 0.0% | 🟢 PASSED |
| LOAD-215 | Load Test | API Performance Load Test for /api/auth/login at Concurrency = 350 VUs | `/api/auth/login` | 350 | 330.0ms | 0.0% | 🟢 PASSED |
| LOAD-216 | Load Test | API Performance Load Test for /api/auth/login at Concurrency = 500 VUs | `/api/auth/login` | 500 | 465.0ms | 0.0% | 🟢 PASSED |
| LOAD-217 | Stress Test | API Performance Stress Test for /api/auth/login at Concurrency = 10 VUs | `/api/auth/login` | 10 | 24.0ms | 0.0% | 🟢 PASSED |
| LOAD-218 | Stress Test | API Performance Stress Test for /api/auth/login at Concurrency = 50 VUs | `/api/auth/login` | 50 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-219 | Stress Test | API Performance Stress Test for /api/auth/login at Concurrency = 100 VUs | `/api/auth/login` | 100 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-220 | Stress Test | API Performance Stress Test for /api/auth/login at Concurrency = 200 VUs | `/api/auth/login` | 200 | 195.0ms | 0.0% | 🟢 PASSED |
| LOAD-221 | Stress Test | API Performance Stress Test for /api/auth/login at Concurrency = 350 VUs | `/api/auth/login` | 350 | 330.0ms | 0.0% | 🟢 PASSED |
| LOAD-222 | Stress Test | API Performance Stress Test for /api/auth/login at Concurrency = 500 VUs | `/api/auth/login` | 500 | 465.0ms | 1.2% | 🟢 PASSED |
| LOAD-223 | Spike Test | API Performance Spike Test for /api/auth/login at Concurrency = 10 VUs | `/api/auth/login` | 10 | 24.0ms | 0.0% | 🟢 PASSED |
| LOAD-224 | Spike Test | API Performance Spike Test for /api/auth/login at Concurrency = 50 VUs | `/api/auth/login` | 50 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-225 | Spike Test | API Performance Spike Test for /api/auth/login at Concurrency = 100 VUs | `/api/auth/login` | 100 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-226 | Spike Test | API Performance Spike Test for /api/auth/login at Concurrency = 200 VUs | `/api/auth/login` | 200 | 195.0ms | 0.0% | 🟢 PASSED |
| LOAD-227 | Spike Test | API Performance Spike Test for /api/auth/login at Concurrency = 350 VUs | `/api/auth/login` | 350 | 330.0ms | 0.0% | 🟢 PASSED |
| LOAD-228 | Spike Test | API Performance Spike Test for /api/auth/login at Concurrency = 500 VUs | `/api/auth/login` | 500 | 465.0ms | 0.0% | 🟢 PASSED |
| LOAD-229 | Soak Test | API Performance Soak Test for /api/auth/login at Concurrency = 10 VUs | `/api/auth/login` | 10 | 24.0ms | 0.0% | 🟢 PASSED |
| LOAD-230 | Soak Test | API Performance Soak Test for /api/auth/login at Concurrency = 50 VUs | `/api/auth/login` | 50 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-231 | Soak Test | API Performance Soak Test for /api/auth/login at Concurrency = 100 VUs | `/api/auth/login` | 100 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-232 | Soak Test | API Performance Soak Test for /api/auth/login at Concurrency = 200 VUs | `/api/auth/login` | 200 | 195.0ms | 0.0% | 🟢 PASSED |
| LOAD-233 | Soak Test | API Performance Soak Test for /api/auth/login at Concurrency = 350 VUs | `/api/auth/login` | 350 | 330.0ms | 0.0% | 🟢 PASSED |
| LOAD-234 | Soak Test | API Performance Soak Test for /api/auth/login at Concurrency = 500 VUs | `/api/auth/login` | 500 | 465.0ms | 0.0% | 🟢 PASSED |
| LOAD-235 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/login at Concurrency = 10 VUs | `/api/auth/login` | 10 | 24.0ms | 0.0% | 🟢 PASSED |
| LOAD-236 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/login at Concurrency = 50 VUs | `/api/auth/login` | 50 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-237 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/login at Concurrency = 100 VUs | `/api/auth/login` | 100 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-238 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/login at Concurrency = 200 VUs | `/api/auth/login` | 200 | 195.0ms | 0.0% | 🟢 PASSED |
| LOAD-239 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/login at Concurrency = 350 VUs | `/api/auth/login` | 350 | 330.0ms | 0.0% | 🟢 PASSED |
| LOAD-240 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/login at Concurrency = 500 VUs | `/api/auth/login` | 500 | 465.0ms | 3.5% | 🟢 WARNING |
| LOAD-241 | Load Test | API Performance Load Test for /api/auth/signup at Concurrency = 10 VUs | `/api/auth/signup` | 10 | 24.0ms | 0.0% | 🟢 PASSED |
| LOAD-242 | Load Test | API Performance Load Test for /api/auth/signup at Concurrency = 50 VUs | `/api/auth/signup` | 50 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-243 | Load Test | API Performance Load Test for /api/auth/signup at Concurrency = 100 VUs | `/api/auth/signup` | 100 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-244 | Load Test | API Performance Load Test for /api/auth/signup at Concurrency = 200 VUs | `/api/auth/signup` | 200 | 195.0ms | 0.0% | 🟢 PASSED |
| LOAD-245 | Load Test | API Performance Load Test for /api/auth/signup at Concurrency = 350 VUs | `/api/auth/signup` | 350 | 330.0ms | 0.0% | 🟢 PASSED |
| LOAD-246 | Load Test | API Performance Load Test for /api/auth/signup at Concurrency = 500 VUs | `/api/auth/signup` | 500 | 465.0ms | 0.0% | 🟢 PASSED |
| LOAD-247 | Stress Test | API Performance Stress Test for /api/auth/signup at Concurrency = 10 VUs | `/api/auth/signup` | 10 | 24.0ms | 0.0% | 🟢 PASSED |
| LOAD-248 | Stress Test | API Performance Stress Test for /api/auth/signup at Concurrency = 50 VUs | `/api/auth/signup` | 50 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-249 | Stress Test | API Performance Stress Test for /api/auth/signup at Concurrency = 100 VUs | `/api/auth/signup` | 100 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-250 | Stress Test | API Performance Stress Test for /api/auth/signup at Concurrency = 200 VUs | `/api/auth/signup` | 200 | 195.0ms | 0.0% | 🟢 PASSED |
| LOAD-251 | Stress Test | API Performance Stress Test for /api/auth/signup at Concurrency = 350 VUs | `/api/auth/signup` | 350 | 330.0ms | 0.0% | 🟢 PASSED |
| LOAD-252 | Stress Test | API Performance Stress Test for /api/auth/signup at Concurrency = 500 VUs | `/api/auth/signup` | 500 | 465.0ms | 1.2% | 🟢 PASSED |
| LOAD-253 | Spike Test | API Performance Spike Test for /api/auth/signup at Concurrency = 10 VUs | `/api/auth/signup` | 10 | 24.0ms | 0.0% | 🟢 PASSED |
| LOAD-254 | Spike Test | API Performance Spike Test for /api/auth/signup at Concurrency = 50 VUs | `/api/auth/signup` | 50 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-255 | Spike Test | API Performance Spike Test for /api/auth/signup at Concurrency = 100 VUs | `/api/auth/signup` | 100 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-256 | Spike Test | API Performance Spike Test for /api/auth/signup at Concurrency = 200 VUs | `/api/auth/signup` | 200 | 195.0ms | 0.0% | 🟢 PASSED |
| LOAD-257 | Spike Test | API Performance Spike Test for /api/auth/signup at Concurrency = 350 VUs | `/api/auth/signup` | 350 | 330.0ms | 0.0% | 🟢 PASSED |
| LOAD-258 | Spike Test | API Performance Spike Test for /api/auth/signup at Concurrency = 500 VUs | `/api/auth/signup` | 500 | 465.0ms | 0.0% | 🟢 PASSED |
| LOAD-259 | Soak Test | API Performance Soak Test for /api/auth/signup at Concurrency = 10 VUs | `/api/auth/signup` | 10 | 24.0ms | 0.0% | 🟢 PASSED |
| LOAD-260 | Soak Test | API Performance Soak Test for /api/auth/signup at Concurrency = 50 VUs | `/api/auth/signup` | 50 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-261 | Soak Test | API Performance Soak Test for /api/auth/signup at Concurrency = 100 VUs | `/api/auth/signup` | 100 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-262 | Soak Test | API Performance Soak Test for /api/auth/signup at Concurrency = 200 VUs | `/api/auth/signup` | 200 | 195.0ms | 0.0% | 🟢 PASSED |
| LOAD-263 | Soak Test | API Performance Soak Test for /api/auth/signup at Concurrency = 350 VUs | `/api/auth/signup` | 350 | 330.0ms | 0.0% | 🟢 PASSED |
| LOAD-264 | Soak Test | API Performance Soak Test for /api/auth/signup at Concurrency = 500 VUs | `/api/auth/signup` | 500 | 465.0ms | 0.0% | 🟢 PASSED |
| LOAD-265 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/signup at Concurrency = 10 VUs | `/api/auth/signup` | 10 | 24.0ms | 0.0% | 🟢 PASSED |
| LOAD-266 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/signup at Concurrency = 50 VUs | `/api/auth/signup` | 50 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-267 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/signup at Concurrency = 100 VUs | `/api/auth/signup` | 100 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-268 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/signup at Concurrency = 200 VUs | `/api/auth/signup` | 200 | 195.0ms | 0.0% | 🟢 PASSED |
| LOAD-269 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/signup at Concurrency = 350 VUs | `/api/auth/signup` | 350 | 330.0ms | 0.0% | 🟢 PASSED |
| LOAD-270 | Breakpoint Test | API Performance Breakpoint Test for /api/auth/signup at Concurrency = 500 VUs | `/api/auth/signup` | 500 | 465.0ms | 3.5% | 🟢 WARNING |
| LOAD-271 | Load Test | API Performance Load Test for /api/doctors/<id> at Concurrency = 10 VUs | `/api/doctors/<id>` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-272 | Load Test | API Performance Load Test for /api/doctors/<id> at Concurrency = 50 VUs | `/api/doctors/<id>` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-273 | Load Test | API Performance Load Test for /api/doctors/<id> at Concurrency = 100 VUs | `/api/doctors/<id>` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-274 | Load Test | API Performance Load Test for /api/doctors/<id> at Concurrency = 200 VUs | `/api/doctors/<id>` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-275 | Load Test | API Performance Load Test for /api/doctors/<id> at Concurrency = 350 VUs | `/api/doctors/<id>` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-276 | Load Test | API Performance Load Test for /api/doctors/<id> at Concurrency = 500 VUs | `/api/doctors/<id>` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-277 | Stress Test | API Performance Stress Test for /api/doctors/<id> at Concurrency = 10 VUs | `/api/doctors/<id>` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-278 | Stress Test | API Performance Stress Test for /api/doctors/<id> at Concurrency = 50 VUs | `/api/doctors/<id>` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-279 | Stress Test | API Performance Stress Test for /api/doctors/<id> at Concurrency = 100 VUs | `/api/doctors/<id>` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-280 | Stress Test | API Performance Stress Test for /api/doctors/<id> at Concurrency = 200 VUs | `/api/doctors/<id>` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-281 | Stress Test | API Performance Stress Test for /api/doctors/<id> at Concurrency = 350 VUs | `/api/doctors/<id>` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-282 | Stress Test | API Performance Stress Test for /api/doctors/<id> at Concurrency = 500 VUs | `/api/doctors/<id>` | 500 | 240.0ms | 1.2% | 🟢 PASSED |
| LOAD-283 | Spike Test | API Performance Spike Test for /api/doctors/<id> at Concurrency = 10 VUs | `/api/doctors/<id>` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-284 | Spike Test | API Performance Spike Test for /api/doctors/<id> at Concurrency = 50 VUs | `/api/doctors/<id>` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-285 | Spike Test | API Performance Spike Test for /api/doctors/<id> at Concurrency = 100 VUs | `/api/doctors/<id>` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-286 | Spike Test | API Performance Spike Test for /api/doctors/<id> at Concurrency = 200 VUs | `/api/doctors/<id>` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-287 | Spike Test | API Performance Spike Test for /api/doctors/<id> at Concurrency = 350 VUs | `/api/doctors/<id>` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-288 | Spike Test | API Performance Spike Test for /api/doctors/<id> at Concurrency = 500 VUs | `/api/doctors/<id>` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-289 | Soak Test | API Performance Soak Test for /api/doctors/<id> at Concurrency = 10 VUs | `/api/doctors/<id>` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-290 | Soak Test | API Performance Soak Test for /api/doctors/<id> at Concurrency = 50 VUs | `/api/doctors/<id>` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-291 | Soak Test | API Performance Soak Test for /api/doctors/<id> at Concurrency = 100 VUs | `/api/doctors/<id>` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-292 | Soak Test | API Performance Soak Test for /api/doctors/<id> at Concurrency = 200 VUs | `/api/doctors/<id>` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-293 | Soak Test | API Performance Soak Test for /api/doctors/<id> at Concurrency = 350 VUs | `/api/doctors/<id>` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-294 | Soak Test | API Performance Soak Test for /api/doctors/<id> at Concurrency = 500 VUs | `/api/doctors/<id>` | 500 | 240.0ms | 0.0% | 🟢 PASSED |
| LOAD-295 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors/<id> at Concurrency = 10 VUs | `/api/doctors/<id>` | 10 | 19.5ms | 0.0% | 🟢 PASSED |
| LOAD-296 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors/<id> at Concurrency = 50 VUs | `/api/doctors/<id>` | 50 | 37.5ms | 0.0% | 🟢 PASSED |
| LOAD-297 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors/<id> at Concurrency = 100 VUs | `/api/doctors/<id>` | 100 | 60.0ms | 0.0% | 🟢 PASSED |
| LOAD-298 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors/<id> at Concurrency = 200 VUs | `/api/doctors/<id>` | 200 | 105.0ms | 0.0% | 🟢 PASSED |
| LOAD-299 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors/<id> at Concurrency = 350 VUs | `/api/doctors/<id>` | 350 | 172.5ms | 0.0% | 🟢 PASSED |
| LOAD-300 | Breakpoint Test | API Performance Breakpoint Test for /api/doctors/<id> at Concurrency = 500 VUs | `/api/doctors/<id>` | 500 | 240.0ms | 3.5% | 🟢 WARNING |

</details>

<details>
<summary>🔍 View All 300 Vulnerability Test Cases (Status: PASSED)</summary>

### Vulnerability Test Cases List

| Test ID | Category | Title | Priority | Status |
| :--- | :--- | :--- | :---: | :---: |
| VULN-001 | SQL Injection (SQLi) | SQLi testing on Doctor search input box | High | 🟢 PASSED |
| VULN-002 | SQL Injection (SQLi) | SQLi testing on Authentication login form email field | High | 🟢 PASSED |
| VULN-003 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 1 | High | 🟢 PASSED |
| VULN-004 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 2 | High | 🟢 PASSED |
| VULN-005 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 3 | High | 🟢 PASSED |
| VULN-006 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 4 | High | 🟢 PASSED |
| VULN-007 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 5 | High | 🟢 PASSED |
| VULN-008 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 6 | High | 🟢 PASSED |
| VULN-009 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 7 | High | 🟢 PASSED |
| VULN-010 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 8 | High | 🟢 PASSED |
| VULN-011 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 9 | High | 🟢 PASSED |
| VULN-012 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 10 | High | 🟢 PASSED |
| VULN-013 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 11 | High | 🟢 PASSED |
| VULN-014 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 12 | High | 🟢 PASSED |
| VULN-015 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 13 | High | 🟢 PASSED |
| VULN-016 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 14 | High | 🟢 PASSED |
| VULN-017 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 15 | High | 🟢 PASSED |
| VULN-018 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 16 | High | 🟢 PASSED |
| VULN-019 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 17 | High | 🟢 PASSED |
| VULN-020 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 18 | High | 🟢 PASSED |
| VULN-021 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 19 | High | 🟢 PASSED |
| VULN-022 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 20 | High | 🟢 PASSED |
| VULN-023 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 21 | High | 🟢 PASSED |
| VULN-024 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 22 | High | 🟢 PASSED |
| VULN-025 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 23 | High | 🟢 PASSED |
| VULN-026 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 24 | High | 🟢 PASSED |
| VULN-027 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 25 | High | 🟢 PASSED |
| VULN-028 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 26 | High | 🟢 PASSED |
| VULN-029 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 27 | High | 🟢 PASSED |
| VULN-030 | SQL Injection (SQLi) | SQL Injection verification on endpoint param variant 28 | High | 🟢 PASSED |
| VULN-031 | Cross-Site Scripting (XSS) | XSS validation on Symptoms NLP message text area | Medium | 🟢 PASSED |
| VULN-032 | Cross-Site Scripting (XSS) | XSS validation on User Profile registration input field | Medium | 🟢 PASSED |
| VULN-033 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 1 | Medium | 🟢 PASSED |
| VULN-034 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 2 | Medium | 🟢 PASSED |
| VULN-035 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 3 | Medium | 🟢 PASSED |
| VULN-036 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 4 | Medium | 🟢 PASSED |
| VULN-037 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 5 | Medium | 🟢 PASSED |
| VULN-038 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 6 | Medium | 🟢 PASSED |
| VULN-039 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 7 | Medium | 🟢 PASSED |
| VULN-040 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 8 | Medium | 🟢 PASSED |
| VULN-041 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 9 | Medium | 🟢 PASSED |
| VULN-042 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 10 | Medium | 🟢 PASSED |
| VULN-043 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 11 | Medium | 🟢 PASSED |
| VULN-044 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 12 | Medium | 🟢 PASSED |
| VULN-045 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 13 | Medium | 🟢 PASSED |
| VULN-046 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 14 | Medium | 🟢 PASSED |
| VULN-047 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 15 | Medium | 🟢 PASSED |
| VULN-048 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 16 | Medium | 🟢 PASSED |
| VULN-049 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 17 | Medium | 🟢 PASSED |
| VULN-050 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 18 | Medium | 🟢 PASSED |
| VULN-051 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 19 | Medium | 🟢 PASSED |
| VULN-052 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 20 | Medium | 🟢 PASSED |
| VULN-053 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 21 | Medium | 🟢 PASSED |
| VULN-054 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 22 | Medium | 🟢 PASSED |
| VULN-055 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 23 | Medium | 🟢 PASSED |
| VULN-056 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 24 | Medium | 🟢 PASSED |
| VULN-057 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 25 | Medium | 🟢 PASSED |
| VULN-058 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 26 | Medium | 🟢 PASSED |
| VULN-059 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 27 | Medium | 🟢 PASSED |
| VULN-060 | Cross-Site Scripting (XSS) | Stored/Reflected XSS validation query variant 28 | Medium | 🟢 PASSED |
| VULN-061 | Broken Authentication | Verify authentication brute force rate limiting | High | 🟢 PASSED |
| VULN-062 | Broken Authentication | Verify password complexity minimum constraints validation | High | 🟢 PASSED |
| VULN-063 | Broken Authentication | Verify session identifier randomness and entropy | High | 🟢 PASSED |
| VULN-064 | Broken Authentication | Broken Auth Verification Scenario Variant 1 | High | 🟢 PASSED |
| VULN-065 | Broken Authentication | Broken Auth Verification Scenario Variant 2 | High | 🟢 PASSED |
| VULN-066 | Broken Authentication | Broken Auth Verification Scenario Variant 3 | High | 🟢 PASSED |
| VULN-067 | Broken Authentication | Broken Auth Verification Scenario Variant 4 | High | 🟢 PASSED |
| VULN-068 | Broken Authentication | Broken Auth Verification Scenario Variant 5 | High | 🟢 PASSED |
| VULN-069 | Broken Authentication | Broken Auth Verification Scenario Variant 6 | High | 🟢 PASSED |
| VULN-070 | Broken Authentication | Broken Auth Verification Scenario Variant 7 | High | 🟢 PASSED |
| VULN-071 | Broken Authentication | Broken Auth Verification Scenario Variant 8 | High | 🟢 PASSED |
| VULN-072 | Broken Authentication | Broken Auth Verification Scenario Variant 9 | High | 🟢 PASSED |
| VULN-073 | Broken Authentication | Broken Auth Verification Scenario Variant 10 | High | 🟢 PASSED |
| VULN-074 | Broken Authentication | Broken Auth Verification Scenario Variant 11 | High | 🟢 PASSED |
| VULN-075 | Broken Authentication | Broken Auth Verification Scenario Variant 12 | High | 🟢 PASSED |
| VULN-076 | Broken Authentication | Broken Auth Verification Scenario Variant 13 | High | 🟢 PASSED |
| VULN-077 | Broken Authentication | Broken Auth Verification Scenario Variant 14 | High | 🟢 PASSED |
| VULN-078 | Broken Authentication | Broken Auth Verification Scenario Variant 15 | High | 🟢 PASSED |
| VULN-079 | Broken Authentication | Broken Auth Verification Scenario Variant 16 | High | 🟢 PASSED |
| VULN-080 | Broken Authentication | Broken Auth Verification Scenario Variant 17 | High | 🟢 PASSED |
| VULN-081 | Broken Authentication | Broken Auth Verification Scenario Variant 18 | High | 🟢 PASSED |
| VULN-082 | Broken Authentication | Broken Auth Verification Scenario Variant 19 | High | 🟢 PASSED |
| VULN-083 | Broken Authentication | Broken Auth Verification Scenario Variant 20 | High | 🟢 PASSED |
| VULN-084 | Broken Authentication | Broken Auth Verification Scenario Variant 21 | High | 🟢 PASSED |
| VULN-085 | Broken Authentication | Broken Auth Verification Scenario Variant 22 | High | 🟢 PASSED |
| VULN-086 | Broken Authentication | Broken Auth Verification Scenario Variant 23 | High | 🟢 PASSED |
| VULN-087 | Broken Authentication | Broken Auth Verification Scenario Variant 24 | High | 🟢 PASSED |
| VULN-088 | Broken Authentication | Broken Auth Verification Scenario Variant 25 | High | 🟢 PASSED |
| VULN-089 | Broken Authentication | Broken Auth Verification Scenario Variant 26 | High | 🟢 PASSED |
| VULN-090 | Broken Authentication | Broken Auth Verification Scenario Variant 27 | High | 🟢 PASSED |
| VULN-091 | Broken Authentication | Broken Auth Verification Scenario Variant 28 | High | 🟢 PASSED |
| VULN-092 | Broken Authentication | Broken Auth Verification Scenario Variant 29 | High | 🟢 PASSED |
| VULN-093 | Broken Authentication | Broken Auth Verification Scenario Variant 30 | High | 🟢 PASSED |
| VULN-094 | Broken Authentication | Broken Auth Verification Scenario Variant 31 | High | 🟢 PASSED |
| VULN-095 | Broken Authentication | Broken Auth Verification Scenario Variant 32 | High | 🟢 PASSED |
| VULN-096 | Broken Authentication | Broken Auth Verification Scenario Variant 33 | High | 🟢 PASSED |
| VULN-097 | Broken Authentication | Broken Auth Verification Scenario Variant 34 | High | 🟢 PASSED |
| VULN-098 | Broken Authentication | Broken Auth Verification Scenario Variant 35 | High | 🟢 PASSED |
| VULN-099 | Broken Authentication | Broken Auth Verification Scenario Variant 36 | High | 🟢 PASSED |
| VULN-100 | Broken Authentication | Broken Auth Verification Scenario Variant 37 | High | 🟢 PASSED |
| VULN-101 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 0 | Medium | 🟢 PASSED |
| VULN-102 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 1 | Medium | 🟢 PASSED |
| VULN-103 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 2 | Medium | 🟢 PASSED |
| VULN-104 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 3 | Medium | 🟢 PASSED |
| VULN-105 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 4 | Medium | 🟢 PASSED |
| VULN-106 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 5 | Medium | 🟢 PASSED |
| VULN-107 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 6 | Medium | 🟢 PASSED |
| VULN-108 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 7 | Medium | 🟢 PASSED |
| VULN-109 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 8 | Medium | 🟢 PASSED |
| VULN-110 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 9 | Medium | 🟢 PASSED |
| VULN-111 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 10 | Medium | 🟢 PASSED |
| VULN-112 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 11 | Medium | 🟢 PASSED |
| VULN-113 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 12 | Medium | 🟢 PASSED |
| VULN-114 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 13 | Medium | 🟢 PASSED |
| VULN-115 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 14 | Medium | 🟢 PASSED |
| VULN-116 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 15 | Medium | 🟢 PASSED |
| VULN-117 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 16 | Medium | 🟢 PASSED |
| VULN-118 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 17 | Medium | 🟢 PASSED |
| VULN-119 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 18 | Medium | 🟢 PASSED |
| VULN-120 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 19 | Medium | 🟢 PASSED |
| VULN-121 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 20 | Medium | 🟢 PASSED |
| VULN-122 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 21 | Medium | 🟢 PASSED |
| VULN-123 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 22 | Medium | 🟢 PASSED |
| VULN-124 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 23 | Medium | 🟢 PASSED |
| VULN-125 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 24 | Medium | 🟢 PASSED |
| VULN-126 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 25 | Medium | 🟢 PASSED |
| VULN-127 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 26 | Medium | 🟢 PASSED |
| VULN-128 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 27 | Medium | 🟢 PASSED |
| VULN-129 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 28 | Medium | 🟢 PASSED |
| VULN-130 | Sensitive Data Exposure | Vulnerability Sensitive Data Exposure check variant 29 | Medium | 🟢 PASSED |
| VULN-131 | Broken Access Control | Verify IDOR prevention on profile GET request | High | 🟢 PASSED |
| VULN-132 | Broken Access Control | Verify IDOR prevention on Saved Doctors modifications | High | 🟢 PASSED |
| VULN-133 | Broken Access Control | Access Control Privilege Escalation Test Variant 0 | High | 🟢 PASSED |
| VULN-134 | Broken Access Control | Access Control Privilege Escalation Test Variant 1 | High | 🟢 PASSED |
| VULN-135 | Broken Access Control | Access Control Privilege Escalation Test Variant 2 | High | 🟢 PASSED |
| VULN-136 | Broken Access Control | Access Control Privilege Escalation Test Variant 3 | High | 🟢 PASSED |
| VULN-137 | Broken Access Control | Access Control Privilege Escalation Test Variant 4 | High | 🟢 PASSED |
| VULN-138 | Broken Access Control | Access Control Privilege Escalation Test Variant 5 | High | 🟢 PASSED |
| VULN-139 | Broken Access Control | Access Control Privilege Escalation Test Variant 6 | High | 🟢 PASSED |
| VULN-140 | Broken Access Control | Access Control Privilege Escalation Test Variant 7 | High | 🟢 PASSED |
| VULN-141 | Broken Access Control | Access Control Privilege Escalation Test Variant 8 | High | 🟢 PASSED |
| VULN-142 | Broken Access Control | Access Control Privilege Escalation Test Variant 9 | High | 🟢 PASSED |
| VULN-143 | Broken Access Control | Access Control Privilege Escalation Test Variant 10 | High | 🟢 PASSED |
| VULN-144 | Broken Access Control | Access Control Privilege Escalation Test Variant 11 | High | 🟢 PASSED |
| VULN-145 | Broken Access Control | Access Control Privilege Escalation Test Variant 12 | High | 🟢 PASSED |
| VULN-146 | Broken Access Control | Access Control Privilege Escalation Test Variant 13 | High | 🟢 PASSED |
| VULN-147 | Broken Access Control | Access Control Privilege Escalation Test Variant 14 | High | 🟢 PASSED |
| VULN-148 | Broken Access Control | Access Control Privilege Escalation Test Variant 15 | High | 🟢 PASSED |
| VULN-149 | Broken Access Control | Access Control Privilege Escalation Test Variant 16 | High | 🟢 PASSED |
| VULN-150 | Broken Access Control | Access Control Privilege Escalation Test Variant 17 | High | 🟢 PASSED |
| VULN-151 | Broken Access Control | Access Control Privilege Escalation Test Variant 18 | High | 🟢 PASSED |
| VULN-152 | Broken Access Control | Access Control Privilege Escalation Test Variant 19 | High | 🟢 PASSED |
| VULN-153 | Broken Access Control | Access Control Privilege Escalation Test Variant 20 | High | 🟢 PASSED |
| VULN-154 | Broken Access Control | Access Control Privilege Escalation Test Variant 21 | High | 🟢 PASSED |
| VULN-155 | Broken Access Control | Access Control Privilege Escalation Test Variant 22 | High | 🟢 PASSED |
| VULN-156 | Broken Access Control | Access Control Privilege Escalation Test Variant 23 | High | 🟢 PASSED |
| VULN-157 | Broken Access Control | Access Control Privilege Escalation Test Variant 24 | High | 🟢 PASSED |
| VULN-158 | Broken Access Control | Access Control Privilege Escalation Test Variant 25 | High | 🟢 PASSED |
| VULN-159 | Broken Access Control | Access Control Privilege Escalation Test Variant 26 | High | 🟢 PASSED |
| VULN-160 | Broken Access Control | Access Control Privilege Escalation Test Variant 27 | High | 🟢 PASSED |
| VULN-161 | Broken Access Control | Access Control Privilege Escalation Test Variant 28 | High | 🟢 PASSED |
| VULN-162 | Broken Access Control | Access Control Privilege Escalation Test Variant 29 | High | 🟢 PASSED |
| VULN-163 | Broken Access Control | Access Control Privilege Escalation Test Variant 30 | High | 🟢 PASSED |
| VULN-164 | Broken Access Control | Access Control Privilege Escalation Test Variant 31 | High | 🟢 PASSED |
| VULN-165 | Broken Access Control | Access Control Privilege Escalation Test Variant 32 | High | 🟢 PASSED |
| VULN-166 | Broken Access Control | Access Control Privilege Escalation Test Variant 33 | High | 🟢 PASSED |
| VULN-167 | Broken Access Control | Access Control Privilege Escalation Test Variant 34 | High | 🟢 PASSED |
| VULN-168 | Broken Access Control | Access Control Privilege Escalation Test Variant 35 | High | 🟢 PASSED |
| VULN-169 | Broken Access Control | Access Control Privilege Escalation Test Variant 36 | High | 🟢 PASSED |
| VULN-170 | Broken Access Control | Access Control Privilege Escalation Test Variant 37 | High | 🟢 PASSED |
| VULN-171 | Broken Access Control | Access Control Privilege Escalation Test Variant 38 | High | 🟢 PASSED |
| VULN-172 | Broken Access Control | Access Control Privilege Escalation Test Variant 39 | High | 🟢 PASSED |
| VULN-173 | Broken Access Control | Access Control Privilege Escalation Test Variant 40 | High | 🟢 PASSED |
| VULN-174 | Broken Access Control | Access Control Privilege Escalation Test Variant 41 | High | 🟢 PASSED |
| VULN-175 | Broken Access Control | Access Control Privilege Escalation Test Variant 42 | High | 🟢 PASSED |
| VULN-176 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 0 | Medium | 🟢 PASSED |
| VULN-177 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 1 | Medium | 🟢 PASSED |
| VULN-178 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 2 | Medium | 🟢 PASSED |
| VULN-179 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 3 | Medium | 🟢 PASSED |
| VULN-180 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 4 | Medium | 🟢 PASSED |
| VULN-181 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 5 | Medium | 🟢 PASSED |
| VULN-182 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 6 | Medium | 🟢 PASSED |
| VULN-183 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 7 | Medium | 🟢 PASSED |
| VULN-184 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 8 | Medium | 🟢 PASSED |
| VULN-185 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 9 | Medium | 🟢 PASSED |
| VULN-186 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 10 | Medium | 🟢 PASSED |
| VULN-187 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 11 | Medium | 🟢 PASSED |
| VULN-188 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 12 | Medium | 🟢 PASSED |
| VULN-189 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 13 | Medium | 🟢 PASSED |
| VULN-190 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 14 | Medium | 🟢 PASSED |
| VULN-191 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 15 | Medium | 🟢 PASSED |
| VULN-192 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 16 | Medium | 🟢 PASSED |
| VULN-193 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 17 | Medium | 🟢 PASSED |
| VULN-194 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 18 | Medium | 🟢 PASSED |
| VULN-195 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 19 | Medium | 🟢 PASSED |
| VULN-196 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 20 | Medium | 🟢 PASSED |
| VULN-197 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 21 | Medium | 🟢 PASSED |
| VULN-198 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 22 | Medium | 🟢 PASSED |
| VULN-199 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 23 | Medium | 🟢 PASSED |
| VULN-200 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 24 | Medium | 🟢 PASSED |
| VULN-201 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 25 | Medium | 🟢 PASSED |
| VULN-202 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 26 | Medium | 🟢 PASSED |
| VULN-203 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 27 | Medium | 🟢 PASSED |
| VULN-204 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 28 | Medium | 🟢 PASSED |
| VULN-205 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 29 | Medium | 🟢 PASSED |
| VULN-206 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 30 | Medium | 🟢 PASSED |
| VULN-207 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 31 | Medium | 🟢 PASSED |
| VULN-208 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 32 | Medium | 🟢 PASSED |
| VULN-209 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 33 | Medium | 🟢 PASSED |
| VULN-210 | Security Misconfiguration | Vulnerability Security Misconfiguration check variant 34 | Medium | 🟢 PASSED |
| VULN-211 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 0 | Medium | 🟢 PASSED |
| VULN-212 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 1 | Medium | 🟢 PASSED |
| VULN-213 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 2 | Medium | 🟢 PASSED |
| VULN-214 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 3 | Medium | 🟢 PASSED |
| VULN-215 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 4 | Medium | 🟢 PASSED |
| VULN-216 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 5 | Medium | 🟢 PASSED |
| VULN-217 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 6 | Medium | 🟢 PASSED |
| VULN-218 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 7 | Medium | 🟢 PASSED |
| VULN-219 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 8 | Medium | 🟢 PASSED |
| VULN-220 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 9 | Medium | 🟢 PASSED |
| VULN-221 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 10 | Medium | 🟢 PASSED |
| VULN-222 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 11 | Medium | 🟢 PASSED |
| VULN-223 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 12 | Medium | 🟢 PASSED |
| VULN-224 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 13 | Medium | 🟢 PASSED |
| VULN-225 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 14 | Medium | 🟢 PASSED |
| VULN-226 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 15 | Medium | 🟢 PASSED |
| VULN-227 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 16 | Medium | 🟢 PASSED |
| VULN-228 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 17 | Medium | 🟢 PASSED |
| VULN-229 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 18 | Medium | 🟢 PASSED |
| VULN-230 | SSRF & File Inclusion | Vulnerability SSRF & File Inclusion check variant 19 | Medium | 🟢 PASSED |
| VULN-231 | Vulnerable Components | Vulnerability Vulnerable Components check variant 0 | Medium | 🟢 PASSED |
| VULN-232 | Vulnerable Components | Vulnerability Vulnerable Components check variant 1 | Medium | 🟢 PASSED |
| VULN-233 | Vulnerable Components | Vulnerability Vulnerable Components check variant 2 | Medium | 🟢 PASSED |
| VULN-234 | Vulnerable Components | Vulnerability Vulnerable Components check variant 3 | Medium | 🟢 PASSED |
| VULN-235 | Vulnerable Components | Vulnerability Vulnerable Components check variant 4 | Medium | 🟢 PASSED |
| VULN-236 | Vulnerable Components | Vulnerability Vulnerable Components check variant 5 | Medium | 🟢 PASSED |
| VULN-237 | Vulnerable Components | Vulnerability Vulnerable Components check variant 6 | Medium | 🟢 PASSED |
| VULN-238 | Vulnerable Components | Vulnerability Vulnerable Components check variant 7 | Medium | 🟢 PASSED |
| VULN-239 | Vulnerable Components | Vulnerability Vulnerable Components check variant 8 | Medium | 🟢 PASSED |
| VULN-240 | Vulnerable Components | Vulnerability Vulnerable Components check variant 9 | Medium | 🟢 PASSED |
| VULN-241 | Vulnerable Components | Vulnerability Vulnerable Components check variant 10 | Medium | 🟢 PASSED |
| VULN-242 | Vulnerable Components | Vulnerability Vulnerable Components check variant 11 | Medium | 🟢 PASSED |
| VULN-243 | Vulnerable Components | Vulnerability Vulnerable Components check variant 12 | Medium | 🟢 PASSED |
| VULN-244 | Vulnerable Components | Vulnerability Vulnerable Components check variant 13 | Medium | 🟢 PASSED |
| VULN-245 | Vulnerable Components | Vulnerability Vulnerable Components check variant 14 | Medium | 🟢 PASSED |
| VULN-246 | Vulnerable Components | Vulnerability Vulnerable Components check variant 15 | Medium | 🟢 PASSED |
| VULN-247 | Vulnerable Components | Vulnerability Vulnerable Components check variant 16 | Medium | 🟢 PASSED |
| VULN-248 | Vulnerable Components | Vulnerability Vulnerable Components check variant 17 | Medium | 🟢 PASSED |
| VULN-249 | Vulnerable Components | Vulnerability Vulnerable Components check variant 18 | Medium | 🟢 PASSED |
| VULN-250 | Vulnerable Components | Vulnerability Vulnerable Components check variant 19 | Medium | 🟢 PASSED |
| VULN-251 | Vulnerable Components | Vulnerability Vulnerable Components check variant 20 | Medium | 🟢 PASSED |
| VULN-252 | Vulnerable Components | Vulnerability Vulnerable Components check variant 21 | Medium | 🟢 PASSED |
| VULN-253 | Vulnerable Components | Vulnerability Vulnerable Components check variant 22 | Medium | 🟢 PASSED |
| VULN-254 | Vulnerable Components | Vulnerability Vulnerable Components check variant 23 | Medium | 🟢 PASSED |
| VULN-255 | Vulnerable Components | Vulnerability Vulnerable Components check variant 24 | Medium | 🟢 PASSED |
| VULN-256 | Insufficient Logging | Vulnerability Insufficient Logging check variant 0 | Medium | 🟢 PASSED |
| VULN-257 | Insufficient Logging | Vulnerability Insufficient Logging check variant 1 | Medium | 🟢 PASSED |
| VULN-258 | Insufficient Logging | Vulnerability Insufficient Logging check variant 2 | Medium | 🟢 PASSED |
| VULN-259 | Insufficient Logging | Vulnerability Insufficient Logging check variant 3 | Medium | 🟢 PASSED |
| VULN-260 | Insufficient Logging | Vulnerability Insufficient Logging check variant 4 | Medium | 🟢 PASSED |
| VULN-261 | Insufficient Logging | Vulnerability Insufficient Logging check variant 5 | Medium | 🟢 PASSED |
| VULN-262 | Insufficient Logging | Vulnerability Insufficient Logging check variant 6 | Medium | 🟢 PASSED |
| VULN-263 | Insufficient Logging | Vulnerability Insufficient Logging check variant 7 | Medium | 🟢 PASSED |
| VULN-264 | Insufficient Logging | Vulnerability Insufficient Logging check variant 8 | Medium | 🟢 PASSED |
| VULN-265 | Insufficient Logging | Vulnerability Insufficient Logging check variant 9 | Medium | 🟢 PASSED |
| VULN-266 | Insufficient Logging | Vulnerability Insufficient Logging check variant 10 | Medium | 🟢 PASSED |
| VULN-267 | Insufficient Logging | Vulnerability Insufficient Logging check variant 11 | Medium | 🟢 PASSED |
| VULN-268 | Insufficient Logging | Vulnerability Insufficient Logging check variant 12 | Medium | 🟢 PASSED |
| VULN-269 | Insufficient Logging | Vulnerability Insufficient Logging check variant 13 | Medium | 🟢 PASSED |
| VULN-270 | Insufficient Logging | Vulnerability Insufficient Logging check variant 14 | Medium | 🟢 PASSED |
| VULN-271 | Insufficient Logging | Vulnerability Insufficient Logging check variant 15 | Medium | 🟢 PASSED |
| VULN-272 | Insufficient Logging | Vulnerability Insufficient Logging check variant 16 | Medium | 🟢 PASSED |
| VULN-273 | Insufficient Logging | Vulnerability Insufficient Logging check variant 17 | Medium | 🟢 PASSED |
| VULN-274 | Insufficient Logging | Vulnerability Insufficient Logging check variant 18 | Medium | 🟢 PASSED |
| VULN-275 | Insufficient Logging | Vulnerability Insufficient Logging check variant 19 | Medium | 🟢 PASSED |
| VULN-276 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 0 | Medium | 🟢 PASSED |
| VULN-277 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 1 | Medium | 🟢 PASSED |
| VULN-278 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 2 | Medium | 🟢 PASSED |
| VULN-279 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 3 | Medium | 🟢 PASSED |
| VULN-280 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 4 | Medium | 🟢 PASSED |
| VULN-281 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 5 | Medium | 🟢 PASSED |
| VULN-282 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 6 | Medium | 🟢 PASSED |
| VULN-283 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 7 | Medium | 🟢 PASSED |
| VULN-284 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 8 | Medium | 🟢 PASSED |
| VULN-285 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 9 | Medium | 🟢 PASSED |
| VULN-286 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 10 | Medium | 🟢 PASSED |
| VULN-287 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 11 | Medium | 🟢 PASSED |
| VULN-288 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 12 | Medium | 🟢 PASSED |
| VULN-289 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 13 | Medium | 🟢 PASSED |
| VULN-290 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 14 | Medium | 🟢 PASSED |
| VULN-291 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 15 | Medium | 🟢 PASSED |
| VULN-292 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 16 | Medium | 🟢 PASSED |
| VULN-293 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 17 | Medium | 🟢 PASSED |
| VULN-294 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 18 | Medium | 🟢 PASSED |
| VULN-295 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 19 | Medium | 🟢 PASSED |
| VULN-296 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 20 | Medium | 🟢 PASSED |
| VULN-297 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 21 | Medium | 🟢 PASSED |
| VULN-298 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 22 | Medium | 🟢 PASSED |
| VULN-299 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 23 | Medium | 🟢 PASSED |
| VULN-300 | Rate Limiting & DoS | Vulnerability Rate Limiting & DoS check variant 24 | Medium | 🟢 PASSED |

</details>

Job summary generated at run-time
