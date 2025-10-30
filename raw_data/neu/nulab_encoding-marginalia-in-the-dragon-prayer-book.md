[Skip to content](https://cssh.northeastern.edu/nulab/encoding-marginalia-in-the-dragon-prayer-book/#content)
[ Stories](https://cssh.northeastern.edu/nulab/stories)
[Research Projects](https://cssh.northeastern.edu/nulab/category/research-projects/) 04.22.25
By:[Claire Lavarreda](https://cssh.northeastern.edu/student/claire-lavarreda/)
# Encoding Marginalia in the Dragon Prayer Book
## People in this story
  * [ Claire Lavarreda ](https://cssh.northeastern.edu/student/claire-lavarreda/)
  * [ Erika Boeckeler ](https://cssh.northeastern.edu/faculty/erika-boeckeler/)
  * [ Avery Blankenship ](https://cssh.northeastern.edu/student/avery-blankenship/)
  * [ Julia Flanders ](https://cssh.northeastern.edu/faculty/julia-flanders/)


By: Claire Lavarreda, DITI Research Fellow & PhD Candidate in History
Image 1: Pages 0160v and 0161r of the Dragon Prayer Book. On 161r, marginalia is visible, with the word “et” written next to the start of the third line.
I. Overview
The Dragon Prayer Book Project is an ongoing endeavor to study, transcribe, translate, and encode a medieval manuscript at Northeastern University. Led by Dr. [Erika Boeckeler](https://cssh.northeastern.edu/faculty/erika-boeckeler/), the Dragon Prayer Book Project has three main fields of research related to the book, including transcription, conservation, and microbiology. Written and illustrated by Dominican nuns at the Convent of Saint Catherine in Nuremberg Germany, the date of creation is sometime after 1461.1
Over the years, students have been working diligently to transcribe and translate the Dragon Prayer Book according to TEI ([Text Encoding Initiative](https://tei-c.org/)) guidelines. The current Dragon Prayer Book XML schema was created by Dr. [Julia Flanders](https://cssh.northeastern.edu/faculty/julia-flanders/). It was customized from the general TEI guidelines and intended for simple transcription.23
In Fall of 2024, I joined the Dragon Prayer Book Project in a support role as part of my research assistantship with the Digital Integration Teaching Initiative. After speaking with Professor Boeckeler and establishing the current needs of the DPBP, it was determined that a three-fold marginalia project would be ideal, with deliverables to include:
(1). [An inventory ](https://docs.google.com/document/d/1sEuSSfeuewVM0GLT6gXDoyncfZFvZso-oXTBByGBi-0/edit?usp=sharing)of all the marginalia in the Dragon Prayer Book, containing text translations, identification of the language, scribe, and location, and links to translation sources.
(2). A written document detailing categories and methods for encoding the marginalia.
(3). The encoded marginalia as encoded in the Oxygen XML editor & published on GitHub.
In order to gain familiarity with the project, I attended the weekly DPB meetings and practiced translating several pages from Latin to English in Oxygen.4
II. Establishing A Theory of Marginalia for the Dragon Prayer Book Project
In order to develop a method for encoding marginalia, it is necessary to have a theory of marginalia first.5mean
(1). The Dragon Prayer Book Project prioritizes content over form
(2). The encoding process for marginalia must be flexible in order to integrate into the existing encoded pages
(3). The marginalia should be classified beyond “note,” but does not need to be complicated (no need for elements like <[locus](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-locus.html)> or <[decoNote](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-decoNote.html)> at the moment)
With the above guidelines established, I was able to proceed with the rest of my project.
III. Process: Categories, Elements, & Encoding
The first step in the encoding process was to create an inventory of all the marginalia in the DPB. In addition to images of the marginalia and their corresponding page numbers, I added potential definitions, translations, languages, and scribes. The next step was to categorize the nature of the marginalia using general TEI Manuscript Description elements and attributes. <[Note](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-note.html)> is the grounding element, with further specification made through <[corr](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-corr.html)>, <[add](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-add.html)>, <[del](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-del.html)>, <[figure](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-figure.html)>, and <[lang](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-lang.html)>.67
With all marginalia found and categorized, I then chose a “system” for encoding that would prioritize the content of the notes. I decided to model the encoding after the notes system used in the[ Women Writers Project,](https://cssh.northeastern.edu/nulab/wwp/) which places all notes within a <hyperDiv> at the beginning of the [manuscript](https://www.wwp.neu.edu/research/publications/documentation/internal/#!/entry/note_element). These notes are assigned a unique xml:id, which correspond to the individual notes (which have the matching xml:id) throughout the text.8
IV. Results
Image 2:
Image 3
Image 4
Image 5:
Image 6
Image 7
V. Future Considerations & Final Thoughts
The Dragon Prayer Book Project has involved many participants, and will continue to do so. With this in mind, there are several things future students will need to address, including (1). Research on different scribes, (2). Establishment of a personography, which would then entail pointing to scribal personography entries using @hand, (3). Musical annotation, (4). The use of <hyperDiv> versus [<standOff>](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-standOff.html), and (5). Assigning [target ](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-att.pointing.html)attributes with their full pointers. These considerations are also the product of encoding non-linear and manuscript features in TEI, requiring specification for different types of handwriting, script, and authors. Further, students will need to examine the previous encoders’ uses of <choice> and <seg> for marginalia that are scattered throughout the text. 
Given the expansive and ever-changing nature of the project, it is likely that the current marginalia encoding system will need to be adapted and specialized. However, the Dragon Prayer Book Project now has a theory of marginalia and a basic system to build upon, providing a foundation for future annotation work. Links to the final research project follow: the [inventory](https://docs.google.com/document/d/1sEuSSfeuewVM0GLT6gXDoyncfZFvZso-oXTBByGBi-0/edit?tab=t.0), these [guidelines](https://docs.google.com/document/d/1LU1DLTdfrozmtr6jpVkvLr1dr1Q2zUGOdhZl5DQT8qA/edit?usp=sharing), and the edits made in Oxygen, which [are visible on GitHub](https://github.com/NEU-DSG/dragon-prayer-book/commit/933abfed7f198f66fb7bdd8f0cef93383d6251a2).
Endnotes
1. Ian Thomsen, “Deciphering the Medieval Secrets of the Dragon Prayer Book,” Northeastern Global News, <https://news.northeastern.edu/2019/10/03/exploring-dragon-prayer-books-medieval-prayers-and-chants-recited-by-german-nuns/>
2. Julia Flanders, “Dragon Prayer Book Schema,” Github[dragon-prayer-book/schema/dragon_schema.xml at main · bloucha/dragon-prayer-book · GitHub](https://github.com/bloucha/dragon-prayer-book/blob/main/schema/dragon_schema.xml)
3. These include varied note locations (on the top, bottom, or side of a page; over text, etc) and different meanings/intentions (as a correction, addition, unrelated thoughts). I want to thank the brilliant and accomplished Dr. Avery Blankenship for her wonderful explanation of marginalia and encoding. Her insights, resources, crash-course, and advice were critical to this project. For more on Avery, check out her website: <https://www.averyblankenship.com/>. 
4. The translation process is relatively straight-forward and rarely relies on online translators, like Google or DeepL. A student first selects an available page (already transcribed in Latin), opens it in Oxygen, and then searches for the Latin prayer/hymn in the [Office Book for Dominican Sisters](https://archive.org/details/OfficeBookForDominicanSisters/mode/2up), the [Dominican Missal](https://media.musicasacra.com/dominican/dm.pdf) and the [Douay-Rheims Bible](http://drbo.org/), in addition to second-tier sources. The student then enters the English translation in between the <ab type=“translation” xml:id=“p0566_translation” corresp=“p0566_translation“></ab> tags, noting the source used.
5. TEI Consortium, eds. “Manuscript Description,” Guidelines for Electronic Text Encoding and Interchange<http://www.tei-c.org/Vault/P5/1.7.0/doc/tei-p5-doc/en/html/DS.html#DSFLT>
6. “Note” is a general umbrella for all notes and marginalia, which are further defined by <corr> (correction), <add> (addition), <del> (deletion or omission), <figure> (indicating a drawing, table, or some other non-text symbol), and <lang> (referring to the language of the text).
7. While I was creating the inventory, I noted the presence of more than one scribe. However, I am not an expert in medieval German manuscripts, and I felt that encoding the scribal differences was beyond the scope of this project. “Type” was sufficient enough to distinguish between the author’s edits and the general scribal edits. Further research is needed to determine if there are, in fact, several annotators, at which point the DPB Project could consider assigning them unique identifiers and developing a personography.8. Women Writers Project, “[Internal Documentation: <note>](https://www.wwp.neu.edu/research/publications/documentation/internal/#!/entry/note_element),” WWP, 
## More Stories
### [ “A bunch of degenerates:” An exploration of online discourse about problematic sports betting through social network analysis 08.26.2025](https://cssh.northeastern.edu/nulab/sports-betting-social-network-analysis/) ### [ Framing Taste: Digital Food Policy Archive and Food Stories Project 08.25.2025](https://cssh.northeastern.edu/nulab/framing-taste/)
### [AI and Information Literacy: Data Visualization 09.09.25 Research Projects ](https://cssh.northeastern.edu/nulab/ai-and-information-literacy-data-visualization/)
