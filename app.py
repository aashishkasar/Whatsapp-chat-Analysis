import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Prompt bar
st.info("Upload a WhatsApp chat file to analyze. Please make sure the file is in text format.")

# Sidebar
st.sidebar.title("WhatsApp Chat Analyzer")

# Sidebar Instructions
st.sidebar.markdown(
    """
    ### Instructions:
    1. Upload your WhatsApp chat file in `.txt` format.
    2. Select a user or choose "Overall" for group analysis.
    3. Click on "Show Analysis" to generate insights.
    """
)

# File uploader
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # Fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis with respect to", user_list)

    if st.sidebar.button("Show Analysis"):

        # Stats Area
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        # Monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Activity map
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most Busy Day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        sns.heatmap(user_heatmap, ax=ax, cmap="coolwarm")
        st.pyplot(fig)

        # Finding the busiest users in the group (Group level)
        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # WordCloud
        st.title("Word Cloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        ax.axis("off")
        st.pyplot(fig)

        # Most common words
        st.title('Most Common Words')
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.bar(most_common_df[0], most_common_df[1], color='skyblue')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Emoji Analysis
        st.title("Emoji Analysis")
        emoji_df = helper.emoji_helper(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            if not emoji_df.empty:
                st.header("Top Emojis")
                for index, row in emoji_df.head(5).iterrows():
                    st.write(f"{row['Emoji']} : {row['Count']} times")
            else:
                st.write("No emojis found for this user.")

        # Sentiment Analysis
        sentiment_counts = (
            df[df['user'] == selected_user]['sentiment']
            if selected_user != 'Overall' else df['sentiment']
        ).apply(lambda x: 'Positive' if x > 0 else ('Neutral' if x == 0 else 'Negative')).value_counts()

        st.title("Sentiment Analysis")
        fig, ax = plt.subplots()
        ax.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['green', 'orange', 'red'])
        centre_circle = plt.Circle((0, 0), 0.7, color='white', fc='white')
        fig.gca().add_artist(centre_circle)
        ax.axis('equal')
        st.pyplot(fig)

        # Footer
        st.markdown(
            """
            <p style='text-align: center;'>
            &copy; 2025 WhatsApp Chat Analyzer. All rights reserved.<br>
            Developed with ❤️ by <a href="https://github.com/aashishkasar" target="_blank">Aashish</a>.
            </p>
            """,
            unsafe_allow_html=True
        )
