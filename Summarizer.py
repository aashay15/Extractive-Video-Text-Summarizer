import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """
1) What is a transformer and how does it work?
A transformer is an electrical apparatus designed to convert alternating current from one voltage to another. It can be designed to "step up" or "step down" voltages and works on the magnetic induction principle. A transformer has no moving parts and is a completely static solid state device, which insures, under normal operating conditions, a long and trouble-free life. It consists, in its simplest form, of two or more coils of insulated wire wound on a laminated steel core. When voltage is introduced to one coil, called the primary, it magnetizes the iron core. A voltage is then induced in the other coil, called the secondary or output coil. The change of voltage (or voltage ratio) between the primary and secondary depends on the turns ratio of the two coils.
2) What are taps and when are they used?
Taps are provided on some transformers on the high voltage winding to correct for high or low voltage conditions, and still deliver full rated output voltages at the secondary terminals. Standard tap arrangements are at two and one-half and five percent of the rated primary voltage for both high and low voltage conditions. For example, if the transformer has a 480 volt primary and the available fine voltage is running at 504 volts, the primary should be connected to the 5% tap above normal in order that the secondary voltage be maintained at the proper rating. The standard ASA and NEMA designation for taps are "ANFC" (above normal full capacity) and "BNFC" (below normal full capacity).
3) What is the difference between "Insulating", "Isolating", and "Shielded Winding" transformers?
Insulating and isolating transformers are identical. These terms are used to describe the isolation of the primary and secondary windings, or insulation between the two. A shielded transformer is designed with a metallic shield between the primary and secondary windings to attenuate transient noise. This is especially important in critical applications such as computers, process controllers and many other microprocessor controlled devices.
All two, three and four winding transformers are of the insulating or isolating types. Only autotransformers, whose primary and secondary are connected to each other electrically, are not of the insulating or isolating variety.
Tyco Electronics Corporation
Crompton Instruments
1610 Cobb International Parkway, Unit #4 Kennesaw, GA 30152
Tel. 770-425-8903
Fax. 770-423-7194
4) Can transformers be operated at voltages other than nameplate voltages?
In some cases, transformers can be operated at voltages below the nameplate rated voltage. In NO case should a transformer be operated at a voltage in excess of its nameplate rating unless taps are provided for this purpose. When operating below the rated voltage the KVA capacity is reduced correspondingly. For example, if a 480 volt primary transformer with a 240 volt secondary is operated at 240 volts, the secondary voltage is reduced to 120 volts. If the transformer was originally rated 10 KVA, the reduced rating would be 5 KVA, or in direct proportion to the applied voltage.
5) Can 60 Hz transformers be operated at 50 Hz?
ACME transformers rated below 1 KVA can be used on 50 Hz service. Transformers 1 KVA and larger, rated at 60 Hz, should not be used on 50 Hz service due to the higher losses and resultant heat rise. Special designs are required for this service. However, any 50 Hz transformer will operate on a 60 Hz service.
6) Can transformers be used in parallel?
Single phase transformers can be used in parallel only when their impedances and voltages are equal. If unequal voltages are used, a circulating current exists in the closed network between the two transformers which will cause excess heating and result in a shorter life of the transformer. In addition, impedance values of each transformer must be within 7.5% of each other. For example: Transformer A has an impedance of 4%, transformer B which is to be parallel to A must have an impedance between the limits of 3.7% and 4.3%. When paralleling three phase transformers the same precautions must be observed as listed above, plus the angular displacement and phasing between the two transformers must be identical.
7) Can transformers be reverse connected?
Dry type Distribution transformers can be reverse connected without a loss of KVA rating, but there are certain limitations. Transformers rated 1 KVA and larger single phase, 15 KVA and larger three phase can be reverse connected without any adverse affects or loss in KVA capacity. The reason for this limitation in KVA size is, the turns ratio is the same as the voltage ratio. Example: A transformer with a 480 volt input, 240 volt output - can have the output connected to a 240 volt source and thereby become the primary or input to the transformer, then the original 480 volt primary winding will become the output or 480 volt secondary. On transformers rated below 1 KVA single phase there is a turns ratio compensation on the low voltage winding. This means the low voltage winding has a greater voltage than the nameplate voltage indicates at no load. For example, a small single phase transformer having a nameplate voltage of 480 volts primary and 240 volts secondary, would actually have a no load voltage of approximately 250 volts, and a full load voltage of 240 volts. If the 240 volt winding were connected to a 240 volt source, then the output voltage would consequently be approximately 460 volts at no load and approximately 442 volts at full load. As the KVA becomes smaller, the

compensation is greater- resulting in lower output voltages. When one attempts to use these transformers in reverse the transformer will not be harmed; however, the output voltage will be lower than is indicated by the nameplate.
8) Can a Single Phase Transformer be used on a Three Phase source?
Yes. Any single phase transformer can be used on a three phase source by connecting the primary leads to any two wires of a three phase system, regardless of whether the source is three phase 3-wire or three phase 4- wire. The transformer output will be single phase.
9) Can Transformers develop Three Phase power from a Single Phase source?
No. Phase converters or phase shifting devices such as reactors and capacitors are required to convert single phase power to three phase.
10) How do you select transformers?
1. Determine primary voltage and frequency.
2. Determine secondary voltage required.
3. Determine the capacity required in volt-amperes.
This is done by multiplying the load current (amperes) by the load voltage (volts) for single phase. For example: if the load is 40 amperes, such as a motor, and the secondary voltage is 240 volts, then 240 x 40 equals 9600 VA A 10 KVA (10,000 volt-amperes) transformer is required. ALWAYS SELECT THE TRANSFORMER LARGER THAN THE ACTUAL LOAD. This is done for safety purposes and allows for expansion, in case more load is added at a later date. For 3 phase KVA, multiply rated volts x load amps x 1.73 (square root of 3) then divide by 1000.
4. Determine whether taps are required. Taps are usually specified on larger transformers.
5. Use the selection charts in the Acme catalog.
11) What terminations are provided?
Primary and Secondary Terminations are provided on ACME Dry Type Transformers as follows:
No lugs-lead type connection on:
• 0-25 KVA single phase
• 0-15 KVA three phase
• Bus-bar terminations (drilled to NEMA standards)
• 37 1/2-250 KVA single phase

• 25-500 KVA three phase
12) Can 60 Hz transformers be used at higher frequencies?
Transformers can be used at frequencies above 60 Hz up through 400 Hz with no limitations provided nameplate voltages are not exceeded. However, 60 Hz transformers will have less voltage regulation at 400 Hz than 60 Hz.
13) What is meant by regulation in a transformer?
Voltage regulation in transformers is the difference between the no load voltage and the full load voltage. This is usually expressed in terms of percentage. For example: A transformer delivers 100 volts at no load and the voltage drops to 95 volts at full load, the regulation would be 5%. ACME dry type distribution transformers generally have regulation from 2% to 4%, depending on the size and the application for which they are used.
14) What is temperature rise in a transformer?
Temperature rise in a transformer is the temperature of the windings and insulation above the existing ambient or surrounding temperature.
15) What is "Class" in insulation?
Insulation class was the original method used to distinguish insulating materials operating at different temperature levels. Letters were used for different designations. Letter classifications have been replaced by insulation system temperatures in degrees Celsius. The system temperature is the maximum temperature at the hottest spot in the winding (coil). These systems are used by Acme Transformer for a large part of the product line.
"""
#Loading the english stop words (a, the, and, like etc etc)

stopwords = list(STOP_WORDS)

#This is the model for tokenizing words, i haven't dug deep in this
#but at looking at the outputs I found it is just tokenizing the words
#It is a comprehensive model for tokenizing into words as well as sentences

nlp = spacy.load('en_core_web_sm')

doc = nlp(text)

tokens = [token.text for token in doc]
# print(tokens)

#by looking at the punctuations i found new line wasn't added as punctuation so i added
punctuation = punctuation + '\n'
#print(punctuation)

#Just counting the word freq from the article
#Ignoring punctuations and stopwords
#And storing them in dictionary
word_freq = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1


#print(word_freq)

max_freq = max(word_freq.values())
#print(max_freq)

#normalizing the word freq, by dividing the max freq
for word in word_freq.keys():
    word_freq[word] = word_freq[word]/max_freq

#print(word_freq)

#Tokenizing sentences, The sentences were already tokenized by the nlp(text)
sentence_tokens = [sent for sent in doc.sents]
#print(sentence_tokens)

#getting the sentence scores by addind the word freq which are in the sentence
sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_freq.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_freq[word.text.lower()]
            else:
                sentence_scores[sent] += word_freq[word.text.lower()]

#print(sentence_scores)

#selecting 30% of the total sentences as our summary
select_length = int(len(sentence_tokens)*0.3)
#print(select_length)

#What this does is selects the sentences with highest scores which stays in the summary
#This can be done by arranging the sentences by scores in descending and slicing the array
#with the select_length but the online solution contained this so i used this
#i guess its better for time complexeity for bigger texts...

summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
#print(summary)

final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)

print(summary)
print("SUMMARY LEN :")
print(len(summary))




