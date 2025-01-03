# WhatsApp Chat Analysis

This project is a WhatsApp chat analyzer built using Python and Streamlit. It allows you to upload a WhatsApp chat file (in text format), analyze the data, and gain insights into various aspects like message statistics, activity maps, sentiment analysis, word cloud generation, and more.

## Features

- **Top Statistics**: Displays total messages, words, media messages, and links shared.
- **Monthly and Daily Timelines**: Visualize message frequency over time.
- **Activity Map**: Shows the busiest day and month, as well as weekly activity heatmaps.
- **Busiest Users**: Identifies the most active users in the group.
- **Word Cloud**: Generates a word cloud based on the chat messages.
- **Most Common Words**: Displays the top 20 most frequently used words.
- **Emoji Analysis**: Analyzes and displays emojis used by participants.
- **Sentiment Analysis**: Analyzes and visualizes the sentiment (positive, negative, neutral) of messages.

## Demo

You can try out the live demo of this project on (Copy the link and paste it into your browser.) https://whatsapp-chat-analysis-b7ztkmuqysbwinh7ma7vld.streamlit.app/
## Installation

To run this project locally, follow the instructions below:

### Prerequisites

Ensure you have Python 3.10 installed on your machine.

### Step 1: Clone the repository

git clone https://github.com/your-username/whatsapp-chat-analysis.git
cd whatsapp-chat-analysis
### Step 2: Create a virtual environment (optional but recommended)

Copy code :
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
### Step 3: Install the dependencies

Copy code :
pip install -r requirements.txt
### Step 4: Run the app

Copy code :
streamlit run app.py
Visit http://localhost:8501 in your web browser to interact with the app.

## Usage
Upload WhatsApp Chat File: Upload a WhatsApp chat in text format (ensure it is properly formatted).
Select User: Choose the user whose data you want to analyze, or select "Overall" for group-wide analysis.
View Insights: The app will display various analytics such as message statistics, activity timelines, word clouds, emoji usage, and sentiment distribution.

## File Format
The app accepts WhatsApp chat files in plain text format with the following structure:
[Date, Time] - User: Message
Ensure that the chat export is from WhatsApp and in the required format.

## Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
The project uses several Python libraries including Streamlit, Matplotlib, Seaborn, WordCloud, TextBlob, and more.
Special thanks to Streamlit for making it easy to build and deploy this web app.

## Contact
For any questions, feel free to reach out to [aashishkasar2011@example.com].
