# ChatOda
A chat bot developed and trained to answer just like the Author of the Manga "ONE PIECE" does in its Q&amp;A sections on the volumes called SBS!!

It's currently trained up until SBS of the volume 51. Uses the Gemini API as the chat client through Langchain's modules for store chat history and training of the chat. To use you must use your Gemini API key on the ".streamlit/secrets.toml" folder and run it with Streamlit using the command "streamlit run odachat.py". It will use alot of TOKENs, so be aware.

I've gathered all the SBS data using the script extractsbs.py from the onepiece.wiki, so all credits for them for putting together and obviously all credits for Eichiro Oda. The answers provided by this chat, as all AI chats, can have mistakes and must not be taken as a true answer given by Oda.
