import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import requests
import re


st.set_page_config("Home",layout='wide')
# st.title("TEXT GENERATION USING LLM")
# st.snow()


st.markdown("<h1 style='text-align: center;'>TEXT GENERATION USING LLM</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

a=option_menu("",["Introduction" ,"Text Crafting Tool", "Interactive Insights", "FAQ Sampler"], 
              icons=['book', 'Fountain Pen', 'signal_strength' , 'question'], 
              orientation='horizontal', default_index=0,
             styles={"icon":{ "color": "Red", "font-size": "25px"},
                     "nav-link": {"font-size": "25px", "text-align": "center",'color':'Black'}},
                     )



if a=='Introduction':
    import base64
     
    import base64

    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    img = get_img_as_base64(r"C:\Users\nkvir\OneDrive\Desktop\Lab5Batch\ccccccccccccccccccccc.jpeg")
    
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: fixed; /* Changed from 'local' to 'fixed' */
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/png;base64,{img}");
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
    </style>
    """

    import streamlit as st
    st.markdown(page_bg_img, unsafe_allow_html=True)


















    st.markdown("<h1 style='text-decoration: underline;'>TEXT GENERATION USING LLM </h1>", unsafe_allow_html=True)
    st.header("1. What is LLM?")

    image ="C:\\Users\\nkvir\\OneDrive\\Desktop\\Lab5Batch\\llm.webp"
    st.image(image, width=700, caption='Large Language Model')  
    st.write('''
             * A large language model (LLM) is a deep learning algorithm 
             that can perform a variety of natural language processing 
             (NLP) tasks. 
             * Large language models use transformer models 
             and are trained using massive datasets — hence, large. 
             This enables them to recognize, translate, predict, or
              generate text or other content.
             * Large language models are also referred to as neural networks
              (NNs), which are computing systems inspired by the human brain.
              These neural networks work using a network of nodes that are layered, 
             much like neurons.
                 ''')
    

    st.header("2. How to Generate the Text using LLM ? ")
    img=r"C:\Users\nkvir\OneDrive\Desktop\Lab5Batch\text_llm.png"
    st.image(img, width=700, caption='Text Generation')  
    st.write('''
             Large Language Models (LLMs), such as GPT (Generative Pre-trained Transformer) models, generate text by predicting the next word or token in a sequence based on the context provided. These models are trained on vast amounts of text data and learn the statistical patterns and relationships within the language.

                Here's a simplified explanation of how LLMs generate text:

                1. **Tokenization**: The input text is tokenized into smaller units, such as words or subwords, to be processed by the model.

                2. **Contextual Embeddings**: Each token is converted into a high-dimensional vector representation, known as an embedding, that captures its semantic meaning and context within the sentence.

                3. **Prediction**: The model processes the input tokens sequentially, predicting the probability distribution of the next token given the preceding tokens. This prediction is based on the learned patterns from the training data.

                4. **Sampling**: During text generation, the model samples the next token from the predicted probability distribution. Sampling strategies like greedy decoding (selecting the token with the highest probability) or random sampling (selecting a token randomly based on its probability) can be used.

                5. **Repetition and Diversification**: To avoid repetitive or monotonous output, techniques such as nucleus sampling or temperature scaling can be employed to adjust the diversity of the generated text.

                6. **Generation Process**: The model continues predicting tokens sequentially, incorporating the previously generated tokens as context, until a predefined stopping condition is met, such as reaching a maximum length or generating an end-of-sequence token.

                7. **Post-processing**: The generated text may undergo post-processing steps, such as detokenization and formatting, to produce the final output.

               
       ''')
    
    st.header("3. About Project ")
    img2=r"C:\Users\nkvir\OneDrive\Desktop\Lab5Batch\llm-flowchart.png"
    st.image(img2,width=700, caption='Flow-Chart of Text Generation' )

    st.write(''' 

           For our text generation project, we've decided to focus on the rich cultural heritage of India's temples. Our goal is to develop a system that can provide comprehensive information about various temples across India in response to user queries. This system will utilize a Large Language Model (LLM) to generate informative and contextually relevant responses based on the input prompts.

            Here's a breakdown of our approach:

            1. **Topic Selection**: We've chosen the topic of Indian temples due to their immense cultural significance and diversity. India is home to a vast array of temples, each with its unique architecture, history, and religious practices.

            2. **Scope**: Our project aims to cover a wide range of temples located throughout India, spanning different regions, states, and religions. 
                            This inclusivity will provide users with a comprehensive understanding of the temple landscape in India.

            3. **Text Generation System**: We will develop a text generation system that leverages a pre-trained LLM, such as GPT-3, to generate text-based responses. 
                                            This system will be capable of processing user queries related to Indian temples and generating detailed and coherent answers.

            4. **User Interaction**: Users will interact with our system by inputting queries or prompts related to specific temples or topics of interest. 
                                        The system will analyze these prompts and generate informative responses based on the input.For the better user interaction we use the framwork namely Streamlit .It is the web app

            5. **Content Generation**: The LLM will utilize its learned knowledge of language patterns and contextual understanding to generate text that accurately reflects the queried topic. 
                                        This includes providing information about the history, significance, architecture, festivals, and rituals associated with the requested temple.

            6. **Quality Assurance**: To ensure the quality and accuracy of generated responses, we will implement measures such as fine-tuning the LLM on relevant datasets, validating generated content against trusted sources, and implementing user feedback mechanisms.

            7. **Output Presentation**: The generated text will be presented to users in a clear and organized format, allowing them to easily access the information they seek. This may include structured text output, interactive interfaces, or visual aids to enhance user experience.

               
''')
    































from huggingface_hub import HfFolder, get_full_repo_name, create_repo, upload_folder # Authenticate with your Hugging Face account # You will be prompted to enter your username and password 
# login = HfFolder.get_full_repo_nam(path_in_repo="mistralai/Mixtral-8x22B-Instruct-v0.1", repo_id="mistralai/Mixtral-8x22B-Instruct-v0.1", use_auth_token='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')
from huggingface_hub import notebook_login
notebook_login()
import re
import spacy
# !huggingface-cli login
if a=='Text Crafting Tool':
    import base64

    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    img = get_img_as_base64(r"C:\Users\nkvir\OneDrive\Desktop\Lab5Batch\black.avif")

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """

    import streamlit as st
    st.markdown(page_bg_img, unsafe_allow_html=True)


















































    
    def get_video_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

        # Replace with the path to your video file
    video_file = r"C:\Users\nkvir\OneDrive\Desktop\Lab5Batch\llm.mov"

    video_b64 = get_video_as_base64(video_file)

    page_bg_video = f"""
    <style>
    body {{
    margin: 0;
    padding: 0;
    overflow: visible;
    height: 100vh;
    }}

    video {{
    position: cover;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    z-index: -1;
    background: #000; /* Optional background color for non-video areas */
    }}
    </style>

    <video autoplay loop muted src="data:video/mp4;base64,{video_b64}">
    </video>
    """

    st.markdown(page_bg_video, unsafe_allow_html=True)
    from huggingface_hub import HfFolder, get_full_repo_name, create_repo, upload_folder, notebook_login
    import re
    import spacy
    import streamlit as st
    from langchain import HuggingFaceHub

    # Authenticate with your Hugging Face account
    notebook_login()

    # Define function to extract text from generation
    # def extract_text_from_generation(generation_str):
    #     # Use regular expressions to extract the generated text from the string representation of the LLMResult object
    #     match = re.search(r'Generation\(text=\'(.*?)\'\)', generation_str)
    #     if match:
    #         generated_text = match.group(1)
    #         # Remove newline characters from the generated text
    #         generated_text = generated_text.replace('\n', ' ')
    #         # Split the text into question and answer portions
    #         parts = generated_text.split('?')
    #         if len(parts) > 1:
    #             # Return only the answer portion
    #             return ' '.join(parts[1].split()) + '.'
    #         else:
    #             return generated_text + '.'
    #     else:
    #         return None

    # # Streamlit application
    # if __name__ == "__main__":
    #     st.title("Text Crafting Tool")

    #     inp = st.text_input("Search here.. ")

    #     if inp:
    #         llm = HuggingFaceHub(
    #             repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
    #             model_kwargs={'temperature': 0.5, 'max_length': 1000},
    #             huggingfacehub_api_token="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"
    #         )

    #         # Generate text based on user input
    #         generation = llm.generate(prompts=[inp])
    #         if generation:
    #             # Convert the LLMResult object to a string
    #             generation_str = str(generation)
    #             # Extract the generated text from the string
    #             generated_text = extract_text_from_generation(generation_str)
    #             if generated_text:
    #                 nlp = spacy.load('en_core_web_sm')
    #                 doc = nlp(generated_text)
    #                 new_text = ""
    #                 for sent in doc.sents:
    #                     new_text += str(sent) + " "
    #                 st.write("Generated Text:")
    #                 st.write(new_text.strip())
    #             else:
    #                 st.write("Failed to extract text.")
    #         else:
    #             st.write("Failed to generate text.")
    #     else:
    #         st.write("Please enter a prompt.")



    import re
    import spacy
    import streamlit as st
    from huggingface_hub import notebook_login
    from langchain import HuggingFaceHub

    # Authenticate with your Hugging Face account
    notebook_login()

    # Load the spaCy model
    nlp = spacy.load('en_core_web_sm')

    # Function to extract generated text from LLMResult object
    def extract_text_from_generation(generation_str):
        print("Debug: generation_str =", generation_str)  # Debugging line to print the generation string
        # Attempt to extract the text
        match = re.search(r'text\=[\'\"](.*?)[\'\"]', generation_str)
        if match:
            generated_text = match.group(1)
            # Remove newline characters from the generated text
            generated_text = generated_text.replace('\n', ' ')
            # Split the text into question and answer portions
            parts = generated_text.split('?')
            if len(parts) > 1:
                # Return only the answer portion
                return ' '.join(parts[1].split()) + '.'
            else:
                return generated_text + '.'
        else:
            return None

    # Streamlit application
    if __name__ == "__main__":
        st.title("Text Crafting Tool")

        inp = st.text_input("Search here.. ")

        if inp:
            llm = HuggingFaceHub(
                repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
                model_kwargs={'temperature': 0.5, 'max_length': 1000000000},
                huggingfacehub_api_token="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"
            )

            # Generate text based on user input
            generation = llm.generate(prompts=[inp])
            if generation:
                # Convert the LLMResult object to a string
                generation_str = str(generation)
                # Extract the generated text from the string
                generated_text = extract_text_from_generation(generation_str)
                if generated_text:
                    doc = nlp(generated_text)
                    new_text = ""
                    for sent in doc.sents:
                        new_text += str(sent) + " "
                    st.write("Generated Text:")
                    st.write(new_text.strip())
                else:
                    st.write("Failed to extract text.")
            else:
                st.write("Failed to generate text.")
        else:
            st.write("Please enter a prompt.")















































    # inp= st.text_input("Search here.. ")

    # from langchain import HuggingFaceHub
    # llm = HuggingFaceHub(
    #     repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
    #     model_kwargs={'temperature': 0.5, 'max_length': 10000},
    #     huggingfacehub_api_token="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"
    # )
    # def shortAnswer(ans):
    #     text=ans
    #     pattern = r'\[/INST\](.*?)(?=\d+\s*\[INST\]|$)'
    #     matches = re.findall(pattern, text, re.DOTALL)
    
    #     for match in matches:
    #         answer = match.strip()
    #         sentences = re.split(r'(?<=[.?!])\s+', answer)
    #         # sentences = re.split(r'(?<=\[.?!\])\s+|^\d+\.\s*', answer)
    #         shortened_answer = ' '.join(sentences[:4])
    #         return shortened_answer

    # def getResponse(text):
    #     prompt = text
    #     response = requests.post('https://9238-35-193-63-152.ngrok-free.app/', data={"prompt": prompt})

    #     if response.status_code == 200:
    #         # answer=shortAnswer(response.text)
    #         answer=response.text

    #         return answer
    #     else:
    #         return (f"some Error: {response.status_code}")


    # if inp:
    #         # Generate text based on user input
    #     ans= getResponse(inp)
    #     st.write(ans)
    # else:
    #         st.write("Please enter a prompt.")


#     from huggingface_hub import HfFolder, get_full_repo_name, create_repo, upload_folder, notebook_login
# import re
# import spacy
# import streamlit as st
# from langchain import HuggingFaceHub

# # Authenticate with your Hugging Face account
# notebook_login()

# # Define function to extract text from generation
# def extract_text_from_generation(generation_str):
#     # Use regular expressions to extract the generated text from the string representation of the LLMResult object
#     match = re.search(r'Generation\(text=\'(.*?)\'\)', generation_str)
#     if match:
#         generated_text = match.group(1).strip()  # Remove leading and trailing whitespace including newlines
#         # Remove newline characters from the generated text
#         generated_text = generated_text.replace('\n', ' ')
#         # Split the text into question and answer portions
#         parts = generated_text.split('?')
#         if len(parts) > 1:
#             # Return only the answer portion
#             return ' '.join(parts[1].split()).strip() + '.'  # Join split parts and remove extra spaces
#         else:
#             return generated_text + '.'
#     else:
#         return None

    # Streamlit application

















if a=="FAQ Sampler":
    import base64



    
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    img = get_img_as_base64(r"C:\Users\nkvir\OneDrive\Desktop\Lab5Batch\AI BEAU.jpeg")

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """

    import streamlit as st
    st.markdown(page_bg_img, unsafe_allow_html=True)


    



    import base64
    import streamlit as st

    def get_video_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

        # Replace with the path to your video file
    video_file = r"C:\Users\nkvir\OneDrive\Desktop\Lab5Batch\llm.mov"

    video_b64 = get_video_as_base64(video_file)

    page_bg_video = f"""
    <style>
    body {{
    margin: 0;
    padding: 0;
    overflow: visible;
    height: 100vh;
    }}

    video {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    z-index: -1;
    background: #000; /* Optional background color for non-video areas */
    }}
    </style>

    <video autoplay loop muted src="data:video/mp4;base64,{video_b64}">
    </video>
    """

    st.markdown(page_bg_video, unsafe_allow_html=True)



    o=[2,4,6]
    b=st.selectbox("Select number of Sample FAQ", options=o)
    if b==2:
        st.write("***You Selected 2 sampler of FAQ***")
        st.write('''
                  


            **Question 1: What is the significance of the Tirupati Balaji Temple?**
            Answer: The Tirupati Balaji Temple, located in Andhra Pradesh, is one of the most revered temples in India dedicated to Lord Venkateswara. It is believed to be the richest temple in the world and attracts millions of pilgrims annually. The temple is renowned for its architectural beauty and is considered a sacred pilgrimage site for Hindus.

                 

            **Question 2: When was the Kashi Vishwanath Temple in Varanasi constructed?**
            Answer: The Kashi Vishwanath Temple, also known as the Golden Temple, is one of the oldest and most famous temples in Varanasi, Uttar Pradesh. It is believed to have been constructed in the 11th century by King Vikramaditya. The temple is dedicated to Lord Shiva and is considered one of the holiest Hindu temples in India.
 ''')
        
    if b==4:
        st.write("***You Selected 4 sampler of FAQ***")    
        st.write(''' 
           


            **Question 1 : What is the significance of the Tirupati Balaji Temple?**
            Answer: The Tirupati Balaji Temple, located in Andhra Pradesh, is one of the most revered temples in India dedicated to Lord Venkateswara. It is believed to be the richest temple in the world and attracts millions of pilgrims annually. The temple is renowned for its architectural beauty and is considered a sacred pilgrimage site for Hindus.

                 

            **Question 2 : When was the Kashi Vishwanath Temple in Varanasi constructed?**
            Answer: The Kashi Vishwanath Temple, also known as the Golden Temple, is one of the oldest and most famous temples in Varanasi, Uttar Pradesh. It is believed to have been constructed in the 11th century by King Vikramaditya. The temple is dedicated to Lord Shiva and is considered one of the holiest Hindu temples in India.

                 

            **Question 3 : What are the architectural features of the Brihadeeswarar Temple in Tamil Nadu?**
            Answer: The Brihadeeswarar Temple, also known as the Big Temple, is an architectural marvel located in Thanjavur, Tamil Nadu. Built during the Chola dynasty in the 11th century, the temple is renowned for its towering vimana (tower), which is one of the tallest in the world. The temple's intricate carvings, gopurams (gateway towers), and sculptures depict scenes from Hindu mythology and are exemplary of Dravidian architecture.

                 

            **Question 4 : Which festival is celebrated with great fervor at the Jagannath Temple in Puri?**
            Answer: The Jagannath Temple in Puri, Odisha, is famous for the annual Rath Yatra, or Chariot Festival. This grand festival, held in the Hindu month of Ashadha (June-July), involves the ceremonial procession of Lord Jagannath, his brother Balabhadra, and sister Subhadra in elaborately decorated chariots. It attracts millions of devotees from across the country who come to witness and participate in the divine event.


             ''')
        


    if b==6:
        st.write("***You Selected 6 sampler of FAQ***")    
        st.write(''' 
                 
              


            **Question 1 : What is the legend associated with the origin of the Vaishno Devi Temple in Jammu and Kashmir?**
            Answer: The Vaishno Devi Temple is situated in the Trikuta Mountains of Jammu and Kashmir. According to legend, Mata Vaishno Devi, an incarnation of the Hindu Goddess Mahalakshmi, took refuge in these mountains to escape the demon Bhairon Nath. The temple is visited by millions of devotees each year who undertake a rigorous pilgrimage to seek blessings from the divine mother.

                 

            **Question 2 : How old is the Konark Sun Temple in Odisha, and what is its architectural style?**
            Answer: The Konark Sun Temple, built in the 13th century by King Narasimhadeva I of the Eastern Ganga dynasty, is a UNESCO World Heritage Site located in Konark, Odisha. The temple is renowned for its intricate carvings depicting various aspects of Hindu mythology, as well as its unique architectural style known as Kalinga architecture. It is designed in the shape of a colossal chariot with intricately carved stone wheels, horses, and elephants.

                 

            **Question 3 : What is the significance of the Meenakshi Amman Temple in Madurai, Tamil Nadu?**
            Answer: The Meenakshi Amman Temple, dedicated to Goddess Meenakshi (a form of Parvati) and her consort Lord Sundareswarar (a form of Shiva), is a historic Hindu temple located in Madurai, Tamil Nadu. The temple is renowned for its towering gopurams (gateway towers) adorned with thousands of colorful sculptures and intricate carvings. It is considered one of the finest examples of Dravidian architecture and is a major pilgrimage site in South India.

                 

            **Question 4 : Which deity is worshipped at the Siddhivinayak Temple in Mumbai, Maharashtra?**
            Answer: The Siddhivinayak Temple, located in Prabhadevi, Mumbai, is dedicated to Lord Ganesha, the remover of obstacles and the god of wisdom and prosperity. The temple is one of the richest temples in Mumbai and is visited by thousands of devotees daily. It is particularly popular among devotees seeking blessings for success, prosperity, and the removal of obstacles in their lives.

                 

            **Question 5 : What are the architectural features of the Dilwara Temples in Mount Abu, Rajasthan?**
            Answer: The Dilwara Temples are a group of five Jain temples located in Mount Abu, Rajasthan. Built between the 11th and 13th centuries, these temples are renowned for their exquisite marble carvings, intricate architecture, and detailed craftsmanship. The temples are dedicated to various Jain Tirthankaras and are considered among the most beautiful Jain pilgrimage sites in India.
                 


            **Question 6 : What are the famous festivals celebrated at the Padmanabhaswamy Temple in Thiruvananthapuram, Kerala?**
            Answer: The Padmanabhaswamy Temple, dedicated to Lord Vishnu, hosts several festivals throughout the year. The most prominent festival is the Navratri festival, during which elaborate rituals and cultural performances take place. The temple also celebrates the annual Alpashy festival and Lakshadeepam festival with great pomp and fervor.     


                ''')    
        

    st.write(a)



































if a=='Interactive Insights':
    import base64
     
    

    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    img = get_img_as_base64(r"C:\Users\nkvir\OneDrive\Desktop\Lab5Batch\a11111111111111111.jpeg")
    
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: fixed; /* Changed from 'local' to 'fixed' */
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/png;base64,{img}");
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
    </style>
    """

    import streamlit as st
    st.markdown(page_bg_img, unsafe_allow_html=True)
































    st.write("**Let's delve into the intricacies of text generation with the aid of visualization, refining comprehension and clarity in the process.**")    
    r=st.radio("Select the Visiualization", ['Map', 'Line Chart', 'Bar Chart', 'Pie Chart', 'Bubble Chart'])
    df = st.file_uploader("Upload the dataset")

    if r=='Map':
        st.write("**YOU SELECTED** : ",r )
        st.write(''' 


           **Map Visualization:**

        Geographical Distribution: Plot the locations of temples on a map of India to visualize their geographical distribution. This can help identify clusters of temples in specific regions and provide context for regional variations in temple architecture and culture.
        Heatmap of Temple Density: Create a heatmap showing the density of temples across different regions of India, with color intensity indicating the concentration of temples in each area.
    ''' )    
        
        import pandas as pd
        st.map(df)





    if r=='Line Chart':
        st.write("**YOU SELECTED** : ",r )
        st.write('''
                  **Line Chart:**

            Temporal Trends: Plot the number of temples built over time to visualize temporal trends in temple construction. This can highlight periods of significant temple-building activity or historical events impacting temple construction.
            Comparison of Temple Counts: Create a line chart comparing the growth of temples in different states or regions over time, providing insights into regional variations in temple development.

''')
            

        import pandas as pd
        from streamlit_echarts import st_echarts

        # Load data from CSV file
        df = pd.read_csv("NewAncientTemples.csv")

        # Extract data and categories from the DataFrame
        data = df['DistanceFromMumbai(Km)'].tolist()
        categories = df['templeName'].tolist()

        option = {
        'backgroundColor': '#2c343c',
        'title': {
            'text': 'Line Chart ',
            'left': 'center',
            'top': 20,
            'textStyle': {
            'color': '#ccc'
            }
        },
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
            'type': 'line'
            }
        },
        'xAxis': {
            'type': 'category',
            'data': categories,
            'axisLine': {
            'lineStyle': {
                'color': '#ccc'
            }
            }
        },
        'yAxis': {
            'type': 'value',
            'axisLine': {
            'lineStyle': {
                'color': '#ccc'
            }
            },
            'splitLine': {
            'lineStyle': {
                'color': '#aaa'
            }
            }
        },
        'series': [
            {
            'name': 'Data',
            'type': 'line',
            'data': data,
            'itemStyle': {
                'color': '#E3B3A9',
                'shadowBlur': 200,
                'shadowColor': 'rgba(0, 0, 0, 0.5)'
            }
            }
        ]
        }

        st_echarts(
            options=option, height="600px",
        )



    if r=='Bar Chart':
        st.write("**YOU SELECTED** : ",r )
        st.write('''

        **Bar Chart:**

        Temple Distribution by State: Create a bar chart showing the number of temples in each state of India. This provides an overview of temple distribution across different regions.
        Top States with Most Temples: Highlight the top states with the highest number of temples using a horizontal bar chart, allowing users to easily compare temple counts.
''')
        import pandas as pd
        from streamlit_echarts import st_echarts

        # Load data from CSV file
        df = pd.read_csv("NewAncientTemples.csv")

        # Extract data and categories from the DataFrame
        data = df['DistanceFromMumbai(Km)'].tolist()
        categories = df['templeName'].tolist()

        option = {
            'backgroundColor': '#2c343c',
            'title': {
                'text': 'Bar Chart',
                'left': 'center',
                'top': 20,
                'textStyle': {
                    'color': '#ccc'
                }
            },
            'tooltip': {
                'trigger': 'axis',
                'axisPointer': {
                    'type': 'shadow'
                }
            },
            'xAxis': {
                'type': 'category',
                'data': categories,
                'axisLine': {
                    'lineStyle': {
                        'color': '#ccc'
                    }
                }
            },
            'yAxis': {
                'type': 'value',
                'axisLine': {
                    'lineStyle': {
                        'color': '#ccc'
                    }
                },
                'splitLine': {
                    'lineStyle': {
                        'color': '#aaa'
                    }
                }
            },
            'series': [
                {
                    'name': 'Data',
                    'type': 'bar',  # Changed to bar chart type
                    'data': data,
                    'itemStyle': {
                        'color': '#E3B3A9',
                        'shadowBlur': 200,
                        'shadowColor': 'rgba(0, 0, 0, 0.5)'
                    }
                }
            ]
        }

        st_echarts(
            options=option, height="600px",
        )
   
    
    if r=='Pie Chart':
        st.write("**YOU SELECTED** : ",r )
        st.write('''
            **Pie Chart:**

            Distribution of Temple Types: Use a pie chart to illustrate the proportion of different temple types, such as Hindu temples, Jain temples, Buddhist temples, etc., in the dataset.
            Architectural Styles Breakdown: Visualize the distribution of temple architectural styles, such as Dravidian, Nagara, and Vesara, as segments of a pie chart, showing the relative prevalence of each style.

''')



        import pandas as pd
        from streamlit_echarts import st_echarts

        # Load data from CSV file
        df = pd.read_csv("NewAncientTemples.csv")

        # Extract data and categories from the DataFrame
        data = df['DistanceFromMumbai(Km)'].tolist()
        categories = df['templeName'].tolist()

        option = {
            'backgroundColor': '#2c343c',
            'title': {
                'text': 'Pie Chart',  # Changed title to Pie Chart
                'left': 'center',
                'top': 20,
                'textStyle': {
                    'color': '#ccc'
                }
            },
            'tooltip': {
                'trigger': 'item',
                'formatter': '{a} <br/>{b}: {c} ({d}%)'  # Format tooltip for pie chart
            },
            'series': [
                {
                    'name': 'Data',
                    'type': 'pie',  # Changed to pie chart type
                    'radius': '50%',  # Set radius of the pie chart
                    'center': ['50%', '50%'],  # Center the pie chart
                    'data': [
                        {'value': d, 'name': c} for d, c in zip(data, categories)  # Use data and categories for pie chart
                    ],
                    'label': {
                        'show': True,  # Show labels on the pie chart
                        'formatter': '{b}: {d}%'  # Format label to show category and percentage
                    },
                    'itemStyle': {
                        'emphasis': {
                            'shadowBlur': 20,
                            'shadowOffsetX': 0,
                            'shadowColor': 'rgba(0, 0, 0, 0.5)'  # Add shadow effect to pie chart
                        }
                    }
                }
            ]
        }

        st_echarts(
            options=option, height="600px",
        )
        


    if r=='Bubble Chart':
        st.write("**YOU SELECTED** : ",r )
        st.write('''


            **Bubble Chart:**

            Temple Size vs. Age: Create a bubble chart where each bubble represents a temple, with the x-axis representing the age of the temple and the y-axis representing its size. The size of each bubble can indicate the number of visitors or the level of historical significance.
            Temple Types by Region: Use a bubble chart to visualize the distribution of temple types across different regions of India, with bubble size representing the number of temples in each region and color representing the predominant temple type.
''')
        import pandas as pd
        from streamlit_echarts import st_echarts

        # Load data from CSV file
        df = pd.read_csv("NewAncientTemples.csv")

        # Extract data and categories from the DataFrame
        x_data = df['DistanceFromMumbai(Km)'].tolist()
        y_data = df['DistanceFromNewDelhi(Km)'].tolist()  # Some other data for y-axis
        z_data = df['DistanceFromChennai(Km)'].tolist()  # Some other data for bubble size
        categories = df['templeName'].tolist()

        # Calculate symbol sizes
        symbol_sizes = [z / 10 for z in z_data]

        option = {
            'backgroundColor': '#2c343c',
            'title': {
                'text': 'Bubble Chart',  # Changed title to Bubble Chart
                'left': 'center',
                'top': 20,
                'textStyle': {
                    'color': '#ccc'
                }
            },
            'tooltip': {
                'trigger': 'item',
                'formatter': '{a} <br/>{b}: ({c}, {d}, {e})'  # Format tooltip for bubble chart
            },
            'xAxis': {
                'type': 'value',
                'axisLine': {
                    'lineStyle': {
                        'color': '#ccc'
                    }
                }
            },
            'yAxis': {
                'type': 'value',
                'axisLine': {
                    'lineStyle': {
                        'color': '#ccc'
                    }
                }
            },
            'series': [
                {
                    'name': 'Data',
                    'type': 'scatter',  # Changed to scatter chart type
                    'data': [
                        {'name': c, 'value': [x, y, z], 'symbolSize': s} 
                        for x, y, z, c, s in zip(x_data, y_data, z_data, categories, symbol_sizes)
                    ],  # Use x, y, z coordinates and category for each bubble
                    'label': {
                        'emphasis': {
                            'show': True,
                            'formatter': '{a}: {b}'  # Show name and value in the label when hovered
                        }
                    },
                    'itemStyle': {
                        'emphasis': {
                            'shadowBlur': 20,
                            'shadowOffsetX': 0,
                            'shadowColor': 'rgba(0, 0, 0, 0.5)'  # Add shadow effect to bubbles
                        }
                    }
                }
            ]
        }

        st_echarts(
            options=option, height="600px",
        )

            
    












        











    




    





