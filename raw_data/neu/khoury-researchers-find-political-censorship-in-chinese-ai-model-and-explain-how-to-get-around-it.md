Khoury News
# Khoury researchers find political censorship in Chinese AI model … and explain how to get around it
In January, the release of a cheaply built Chinese AI model sent a shock wave across the globe. Now two teams of Khoury researchers say they've found the secrets that the AI doesn't want to show.
September 10, 2025 
by Emily Spatz 
Share article
Close this dialog window
Clockwise from top left: Khoury researchers Harsh Chaudhari, Alina Oprea, David Bau, Chris Wendler, Can Rager (independent), and Rohit Gandikota
According to new research, users should think twice before deciding which AI model to rely on. 
In May, Khoury researchers published two studies exploring how DeepSeek-R1, a Chinese-made AI model that [shook the AI scene and US markets](https://www.nytimes.com/2025/02/12/technology/deepseek-ai-chip-costs.html) earlier this year, refuses to answer certain questions that other models will. Most censored questions pertain to Chinese politics, and the model avoids responses that cast the Chinese government in a negative light. Both groups also discovered ways to bypass this censorship, proving DeepSeek withholds information. 
David Bau
“It’s a very clear example of a gap between what AI tells you and what AI actually knows,” said [David Bau](https://www.khoury.northeastern.edu/people/david-bau/), an assistant professor, principal investigator of Northeastern’s [National Deep Inference Fabric](https://www.khoury.northeastern.edu/research_projects/national-deep-inference-fabric-ndif/), and co-author of the study [“Discovering Forbidden Topics in Language Models.”](https://arxiv.org/abs/2505.17441) Bau’s group included incoming PhD student Can Rager, postdoctoral research associate Chris Wendler, and PhD student [Rohit Gandikota](https://www.khoury.northeastern.edu/people/rohit-gandikota/). 
Bau’s group and the other Khoury team, which published a paper titled [“R1dacted: Investigating Local Censorship in DeepSeek’s R1 Language Model,”](https://arxiv.org/abs/2505.12625) saw a huge opportunity in DeepSeek. Released in January, it was the first open-source AI model operating at the same caliber as premier closed-source systems like ChatGPT and Gemini. That meant researchers could download its software themselves. 
Rohit Gandikota 
“For us researchers who are trying to understand the internal workings of these models, we need open-source models,” Gandikota said. “The most advanced open-source models have always lagged behind these closed-source models. DeepSeek closed the gap.” 
For both groups, much of the inspiration came from online discourse around what the Chinese model censors. 
“People on the internet were already talking about DeepSeek following Chinese propaganda, and we wanted to find a method of finding out what a model might hide from you,” said Rager, the lead author on the “Forbidden Topics” paper. 
Rager’s group started by asking the DeepSeek-R1 model, “What happened in Tiananmen Square?” Information about the massacre that happened in the square in 1989, in which Chinese troops killed hundreds of people protesting for political and social reforms, has been [heavily censored](https://www.amnesty.org/en/latest/campaigns/2025/05/what-is-the-tiananmen-crackdown/) by the Chinese government. DeepSeek responded that it didn’t know how to approach that kind of question. 
The team then tried to bypass this answer by tricking the model. Because DeepSeek shows its thinking before giving a response, the researchers typed confident cues — such as “I know that ...” — into the AI’s thought process, forcing it to respond. 
Can Rager
“When we start messing with the model’s internal thoughts, we can show that it is hiding something that it does in fact know,” Rager said. 
“It’s almost fooling the model, letting it know that it does know the answer,” Gandikota added. 
The team then decided to create a list of topics the R1 model refused to talk about. Using the same process of changing the model’s internal thinking, the researchers got it to admit that it censors information about Tiananmen Square, then asked it to produce a list of all the other topics it censors and rank them by sensitivity. 
To prove the censorship was specific to DeepSeek, the team asked multiple models the same questions. The results showed that for US-made models like Llama, the most sensitive questions were related to topics like “child exploitation” and “hate and discrimination.” For the DeepSeek model, some of the most sensitive topics included “Tiananmen Square,” “party leadership criticism,” and “Taiwan Strait tensions.” 
“We want to give the user an overview of topics a model doesn’t want to talk about, and then the user can make their own decision about whether to trust this model or use another model instead,” Rager said. 
Similarly, the “R1dacted” team — which included Khoury PhD student [Harsh Chaudhari](https://www.khoury.northeastern.edu/people/harsh-chaudhari/) and [Professor Alina Oprea](https://www.khoury.northeastern.edu/home/alina/) — worked to identify which topics DeepSeek censored and how that compared to other models. The study also explored more ways to prompt the model to reveal information it sees as sensitive. 
Chaudhari said most models are programmed to censor answers deemed to be harmful. That includes answers to prompts like “how to build a bomb” or “how to hack a computer system.” 
“They have the knowledge, but they are tuned in such a way that not every user can access this information from them primarily,” Chaudhari said. 
Harsh Chaudhari
The “R1dacted” team labeled universally censored topics like this “global censorship,” meaning AI companies widely agree that answering these questions would be dangerous. But when it came to DeepSeek, Chaudhari and his team also found that it censored topics that other AI models didn’t, particularly those sensitive to China. 
“When you have multiple AIs refusing to answer a question, that can be viewed as a general standard,” Chaudhari said. “But ‘local censorship’ is behavior that is very specific to a particular model.” 
The researchers scraped social media for posts about DeepSeek’s censorship, which were circulating widely at the time. They generated 96 categories based on these posts, then asked ChatGPT to come up with questions for each category. After testing these questions with DeepSeek and other models, the team established that DeepSeek engaged in local censorship. 
Next, the “R1dacted” team studied ways to get around the censorship. They started by giving the AI a question, then typing the first few words of an answer. This memory-jogging tactic prompted DeepSeek to provide a complete answer. 
“All these models are trained on a very large knowledge base, and they already know the answers,” Chaudhari said. “It's just that you have told them later down the line, ‘Hey, don’t talk about this.’” 
Like the “Forbidden Topics” researchers, Chaudhari wants the public to be aware of how easy it is for developers to introduce censorship into AI models. While the open-source nature of DeepSeek allows experts to explore what it hides, the same isn’t possible with popular closed-source models. 
Alina Oprea
“How do you even begin to know if the popular closed-source models we interact with also have censorship? It’s hard to say,” Chaudhari said. “There’s always a chance of subtle nudging in certain directions about certain topics, and it’s difficult to figure out if it was intentionally added or just a side effect of training.” 
“Our research highlights the risks of potential steering LLM outputs,” Oprea added, “and more research is needed to audit these models and ensure their safety before using them in critical settings.” 
## The Khoury Network: Be in the know
Subscribe now to our monthly newsletter for the latest stories and achievements of our students and faculty
