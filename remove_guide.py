import re

path = r"C:\Users\User\OneDrive\Desktop\MY IA FOR ARTIFICIAL INTELLIGENCE\Iris_Classification_Project\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the tab button
content = re.sub(r'<button\s+type="button"\s+class="analytics-tab-btn"\s+onclick="switchAnalyticsTab\(\'guide\'\)">.*?</button>\s*', '', content)

# 2. Rename the focus button
content = content.replace("🌿 Sepal Length vs Sepal Width (Lecturer Focus)", "🌿 Sepal Length vs Sepal Width")

# 3. Remove view-guide div completely
# It starts at <!-- VIEW 4: LECTURER ORAL DEFENSE GUIDE --> and ends before </section>
pattern = r'<!-- VIEW 4: LECTURER ORAL DEFENSE GUIDE -->.*?</div>\s*</div>\s*</div>\s*(?=</section>)'
content = re.sub(pattern, '', content, flags=re.DOTALL)

# 4. Remove CSS for defense guide
css_pattern = r'/\* Lecturer Defense Guide \*/\s*\.defense-guide-card\s*\{.*?\.(?:defense-qa|defense-q|defense-a).*?\}'
content = re.sub(css_pattern, '', content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done removing lecturer defense guide from index.html")
