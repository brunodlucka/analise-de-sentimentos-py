from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
text_en = analyzer.polarity_scores("BRUNO is smart, handsome, and funny.")
text_pt = analyzer.polarity_scores("BRUNO é inteligente, bonito e engraçado.")
text_esp = analyzer.polarity_scores("BRUNO es inteligente, guapo y divertido.")


print(text_en)
print(text_pt)
print(text_esp)

analyzer = SentimentIntensityAnalyzer()
text_en = analyzer.polarity_scores("I don't like dark chocolate")
text_pt = analyzer.polarity_scores("não gosto de chocolate amargo")
text_esp = analyzer.polarity_scores("no me gusta el chocolate negro")

print(text_en)
print(text_pt)
print(text_esp)

analyzer = SentimentIntensityAnalyzer()
text_en = analyzer.polarity_scores("I'm very happy that I'm going on vacation")
text_pt = analyzer.polarity_scores("I'm very happy that I'm going on vacation")
text_esp = analyzer.polarity_scores("estoy muy feliz de que me voy de vacaciones")

print(text_en)
print(text_pt)
print(text_esp)

analyzer = SentimentIntensityAnalyzer()
text_en = analyzer.polarity_scores("simply my wonderful country Pernambuco")
text_pt = analyzer.polarity_scores("simplesmente meu maravilhoso país Pernambuco")
text_esp = analyzer.polarity_scores("simplemente mi maravilloso país Pernambuco")

print(text_en)
print(text_pt)
print(text_esp)