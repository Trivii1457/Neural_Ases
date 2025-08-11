from transformers import pipeline

class NLPipeline:
    def __init__(self):
        self.summarizer = pipeline("summarization")
        self.question_answerer = pipeline("question-answering")

    def generate_report(self, transcription):
        summary = self.summarize_text(transcription)
        report = self.build_report(transcription, summary)
        return report

    def summarize_text(self, text):
        summary = self.summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']

    def build_report(self, transcription, summary):
        report = {
            "transcription": transcription,
            "summary": summary
        }
        return report

    def answer_question(self, question, context):
        answer = self.question_answerer(question=question, context=context)
        return answer['answer']