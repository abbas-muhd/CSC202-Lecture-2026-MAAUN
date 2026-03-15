#ABBAS MUHAMMAD YUSUF
#MAAUN/24/CSC/0052


from collections import deque

# 1. Initialize
application_inbox = deque()   # queue
processed_history = []        # stack

# 2. Ingest Data
messy_names = [" TechCorp ", "bio-gen", " AI Labs ", "DataHub "]

for name in messy_names:
    clean_name = name.strip().lower()
    application_inbox.append(clean_name)

# 3. Process (FIFO)
while application_inbox:
    app = application_inbox.popleft()
    print("Approving:", app)
    processed_history.append(app)

# 4. Undo (LIFO)
mistake = processed_history.pop()
print("Reverting approval for:", mistake)