# Extractive Video & Text Summarization using KLSummarizer
### This Project is aimed to be used for Online Lecture Summaries and Content Suggestion Relevant to that lecture topic.
The TextSummarizer file can be used to generate Text based Summary of the given subtitles file<br />
The TextSummarizer even suggests online relevant content available for the topic or title of the video lecture(generates it using subtitles file and not the video file itself)<br />
The VideoSummarizer can be used to generate Video Summary given Video(.mp4) and Subtitles(.srt) files.    

## Output : 
The input used is a video file "deep.mp4" that can be downloaded from the outputs folder 

### Video Summarizer Output : 
The output of this code is basically a summary video generated and stored as a mp4. "deep_summary.mp4" is the output generated from my input file and it can be downloaded and viewed in the outputs folder.

The console output is : 
![console output](https://github.com/aashay15/Extractive-Video-Text-Summarizer/blob/master/Outputs/Screenshot%202022-02-01%20at%2012.01.06%20PM.png)

### Text Summarizer Output : 
The text summarizer will generate a text summary and will return relevant links from the topic name (top 3 google search resutls)
In the sample output image below I have used the srt_file (subtitles file) from the deep.mp4 video. The contents of the srt_file are stored as text using the srt_to_txt() function and the operations are carried out on the text.
![text console output](https://github.com/aashay15/Extractive-Video-Text-Summarizer/blob/master/Outputs/Screenshot%202022-02-01%20at%2012.01.05%20PM.png)

