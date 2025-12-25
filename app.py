import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gradio as gr
import o

def analyze(file):


    if file is not None:
        path = file.name
    else:
        path = "study_logs.csv"

    if not os.path.exists(path):
        return "CSV file not found", None, None

    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])

  
    total_minutes = df['Duration_Minutes'].sum()
    total_hours = round(total_minutes / 60, 2)

    avg_daily = round(total_minutes / df['Date'].nunique(), 2)

    most_subject = (
        df.groupby('Subject')['Duration_Minutes']
        .sum()
        .idxmax()
    )

    sessions = len(df)

    summary = (
        f"Total Study Hours: {total_hours}\n"
        f"Average Daily Study (minutes): {avg_daily}\n"
        f"Most Studied Subject: {most_subject}\n"
        f"Total Sessions: {sessions}"
    )

    subject_data = (
        df.groupby('Subject')['Duration_Minutes']
        .sum()
        .reset_index()
    )

    fig1, ax1 = plt.subplots()
    sns.barplot(
        data=subject_data,
        x='Subject',
        y='Duration_Minutes',
        ax=ax1
    )
    plt.xticks(rotation=45)

    daily = (
        df.groupby('Date')['Duration_Minutes']
        .sum()
        .reset_index()
    )

    fig2, ax2 = plt.subplots()
    sns.lineplot(
        data=daily,
        x='Date',
        y='Duration_Minutes',
        ax=ax2
    )

    return summary, fig1, fig2


with gr.Blocks() as app:

    gr.Markdown("##  Online Learning Time Analysis")

    file_input = gr.File(label="Upload CSV (optional)")
    button = gr.Button("Analyze")

    output_text = gr.Textbox(lines=5, label="Summary")
    plot1 = gr.Plot(label="Subject Distribution")
    plot2 = gr.Plot(label="Daily Trend")

    button.click(
        analyze,
        inputs=file_input,
        outputs=[output_text, plot1, plot2]
    )

app.launch()
