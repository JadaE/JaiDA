# jAIda
Jada AI Chat Bot
pronounced "Jada" or "JDA"

# Where am I?
JaiDA is accessible via jadaebong.com/jaida.

# What am I?
AI chat bot

# What am I trying to solve?


# Who would use me?


# How do you interact with me?





[Input Job Description]
        ↓
[Parse Job Requirements with LangChain → OpenAI function calling or extraction chain]
        ↓
[Compare to Uploaded Resume (embedding-based similarity)]
        ↓
[Suggest Edits OR Auto-generate Tailored Resume Section]
        ↓
[Display or Download Tailored Resume]
You can build this with just a few nodes in LangGraph and use LangChain’s load_summarize_chain, LLMChain, and ConversationalRetrievalChain.

For your project, I recommend starting with JSearch API or copy-pasting job posts into your app to skip scraping complexity for now.


will prob need this:
thread = {"configurable": {"thread_id": "1"}} #multiple conversations at one time
# if it's in prod, it will need threads so 2 people can use at one time

Plan and Execute flow pattern!!
make a graph on these steps. a step is a node