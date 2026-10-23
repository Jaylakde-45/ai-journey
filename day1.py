# My AI skills tracker
skills = ['Python','Ml','Dl','Rag','Genai','agents']

# Print each skill with its number
for i,skill in enumerate(skills, 1):
  print(f'{i}: {skill}')

# Add a new skill
skills.append('MLops')
print(f"\nTotal skills: {len(skills)}")

# Check if a skill exists
if 'Rag' in skills:
  print("RAG is in my roadmap")

# Dictionary of AI terms
ai_turms = {
    "AI": "Broad field of smart machine",
    "ML": "Machine learns from data",
    "DL": "Nural Networks",
    "GenAi": "Create new content",
    "Rag": "Retrival + Genration",
    "Agents": "Ai that can act"
}

# Print terms with short definitions
for term, definition in ai_turms.items():
  if len(definition) < 30:
    print(f"{term}: {definition}")
