% Identification
\ProvidesPackage{ProbStatInference}

% This class is based on the standard report class.
% It should have option to process twoside report too.
\LoadClass[fontsize=16pt,a4paper,oneside]{book}
%\documentclass[oneside,12pt,a4paper]{book}
%oneside: to delete bank page

\usepackage{xltxtra}
\usepackage{etoolbox}
%\usepackage{polyglossia}
\usepackage{fontspec}
\usepackage[top=25mm, bottom=20mm, left=25mm, right=20mm]{geometry}
\RequirePackage{titlesec}
\RequirePackage{titletoc}
\XeTeXlinebreaklocale "th"
\XeTeXlinebreakskip = 0pt plus 6pt
\defaultfontfeatures{Scale=1.5}
\RequirePackage{titlesec}
\RequirePackage{titletoc}

\setmainfont[
BoldFont={TH Sarabun New Bold.ttf},
ItalicFont={TH Sarabun New Italic.ttf},
BoldItalicFont={TH Sarabun New Bold Italic.ttf},
]{TH Sarabun New.ttf}


\usepackage[
backend=biber,
bibencoding=utf8,
refsegment=chapter,
citestyle=authoryear,
bibstyle=apa,
firstinits=true,
isbn=false,
doi=false,
url=false,
sorting=none,
clearlang=true,
natbib=true,
date=year
]{biblatex}


\DeclareCiteCommand{\citeauthorfirstlast}
{\boolfalse{citetracker}%
	\boolfalse{pagetracker}%
	\DeclareNameAlias{labelname}{first-last}%
	\usebibmacro{prenote}}
{\ifciteindex
	{\indexnames{labelname}}
	{}%
	\printnames{labelname}}
{\multicitedelim}
{\usebibmacro{postnote}}

\DeclareCiteCommand{\citeauthorlastfirst}
{\boolfalse{citetracker}%
	\boolfalse{pagetracker}%
	\DeclareNameAlias{labelname}{last-first}%
	\usebibmacro{prenote}}
{\ifciteindex
	{\indexnames{labelname}}
	{}%
	\printnames{labelname}}
{\multicitedelim}
{\usebibmacro{postnote}}



\addbibresource{Bibiography.bib}


\linespread{1.5} 

%Add example
\usepackage{amsmath, amsthm}
%\theoremstyle{plain}

\newtheorem{thm}{ทฤษฎีบท}[chapter] % reset theorem numbering for each chapter

\theoremstyle{definition}
\newtheorem{defn}{บทนิยาม}[chapter]  % definition numbers are dependent on theorem numbers
\newtheorem{exmp}[thm]{ตัวอย่าง} % same for example numbers
%\newtheorem{exmp}{Example}[section]

\usepackage[utf8]{inputenc}
\usepackage{enumitem} %adding itemize

% add tables 
\usepackage{multirow}

%add subfigures
\usepackage{graphicx}
\usepackage{subcaption}
\usepackage{adjustbox} %adjusted table

%%insert source in figures
\newcommand*{\captionsource}[2]{%
	\caption[{#1}]{%
		#1%
		\\\hspace{\linewidth}%
		\textbf{ที่มา:} #2%
	}%
}



%\includeonly{CH7_RS_and_itsFunction}

%Page style
\usepackage{fancyhdr}
\newcommand{\setkkuinfofirst}{%
	\pagestyle{fancy}
	\renewcommand\headrulewidth{0pt}
	\lhead{} \chead{} \rhead{} 
	\lfoot{} \cfoot{} \rfoot{}
	\fancyhead[C]{\thepage} % option for twoside
	\pagenumbering{arabic}
}%

%\makeatletter
\renewcommand{\chaptername}{บทที่}
\let\@makechapterhead@ori\@makechapterhead
\renewcommand{\@makechapterhead}[1]{
	\thispagestyle{empty}
	\begin{center} 
		{\large \textbf{ \MakeUppercase\@chapapp\space  ~\thechapter} \\ \textbf{#1}}
	\end{center}
	\vspace{\baselineskip}
}
\makeatother

\def\firstindentlength{1cm}   %% five character aproximate 1 cm
\def\secondindentlength{2cm} 
\def\thirdindentlength{3cm}
\def\fourthindentlength{4cm}

\def\indentitems{2cm}
\setlength{\parindent}{1cm}
\setlength{\itemsep}{1cm}


%section style setup
\renewcommand\thesection{\thechapter.\arabic{section}}
\titleformat{\section}{\bfseries\upshape}{\makebox[\firstindentlength][l]{\thesection}}{0em}{}
\titlespacing{\section}{0ex}{\baselineskip}{\parskip}
% set indent of section
\let\oldsection\section
\def\section{\setlength{\parindent}{\firstindentlength}\oldsection}


%%subsection setup 
\renewcommand\thesubsection{\thesection.\arabic{subsection}}
\titleformat{\subsection}{\bfseries\normalsize\upshape}{\makebox[\firstindentlength][l]{\thesubsection}}{0.4em}{}
\titlespacing{\subsection}{\firstindentlength}{\baselineskip}{\parskip}
% set indent of subsection
\let\oldsubsection\subsection
\def\subsection{\setlength{\parindent}{\secondindentlength}\oldsubsection}


%\newcounter{introChapter}
%\newcommand\introChapter[1]{
%	\thispagestyle{empty}
%	\refstepcounter{introChapter}
%	\begin{center}
%		{\normalsize \textbf{แผนการสอนประจำบทที่ \theintroChapter}}
%	\end{center}
%}

%%%%%%%%%%%% set list description style
\usepackage{enumitem}
\setlist[description]{leftmargin=\indentitems,labelindent=\indentitems}

\setlist[enumerate,1]{leftmargin=\indentitems,labelindent=\indentitems}

%%%%%%%%%%%%%% redefine content name
\renewcommand{\bibname}{REFERENCES}
\renewcommand{\contentsname}{\begin{center} 
				{\LARGE \textbf{สารบัญ}}
			\end{center}
}
\renewcommand{\chaptername}{บทที่}



%%%%%%%%%%%%%%%% set table content format %%%%%%%%%%%%
%\renewcommand{\tableofcontents}{%
%	\begin{center} 
%		{\large \textbf{สารบัญ}}
%	\end{center}
%	\begin{flushright}
%		\textbf{Page}
%	\end{flushright}
%	% Hold current page value
%	% for TOC heading
%	%\@starttoc{toc}%
%}

% A new command to test wheather it is a newpage or not.
% Useful to insert a heading (if possible) for the subsequence pages of the toc
%
% The rests are done by the titletoc package
% I fixed the titledepth to 1 for the sake of simplicity.
% If make it more general -> if more headings -> the entry will be more 
% and one must solve the "Table of Contents (cont.)" on the second page of the TOC.
% In this case, I think the bug is at the Graduate School and I will not fix it.

%\tocheadcont{\tocitem}{\linenumber}{headertype}
\newcommand{\tocheadcont}[3]{
	%\ifthenelse{#1>27 \OR #2>27}{
	\ifthenelse{\intcalcMod{#1}}{
		%\cleardoublepage
		%Should be a newpage here.
		\pagebreak[4]
		%\resetlinenumber[1]
		%\setcounter{tocitem}{0}
		\setcounter{linenumber}{2}
		\begin{center}
			{\large \textbf{#3 (ต่อ)} }
		\end{center} 
		\vspace{\baselineskip}
		\begin{flushright}
			\textbf{Page}
		\end{flushright}
	}{
		\ifthenelse{#1 > 27}{
			\pagebreak[4]
			%\resetlinenumber[1]
			%\setcounter{tocitem}{0}
			\setcounter{linenumber}{2}
			\begin{center}
				{\large \textbf{#3 (ต่อ)} }
			\end{center} 
			\vspace{\baselineskip}
			\begin{flushright}
				\textbf{Page}
			\end{flushright}
		}{}
	}
}

\titlecontents{chapter}[0mm]{\stepcounter{tocitem}\tocheadcont{\thelinenumber}{\thetocitem}{สารบัญ}}{\MakeUppercase\chaptername\hspace{1ex}\thecontentslabel\hspace{2mm}}{}{\hfill \contentspage}

\titlecontents{section}[0mm]{\stepcounter{tocitem}\tocheadcont{\thelinenumber}{\thetocitem}{สารบัญ}}{\hspace{\firstindentlength}\thecontentslabel.\hspace{2mm}}{\hspace{\firstindentlength}\thecontentslabel\hspace{2mm}}{\hfill \contentspage} 







%%%%%%%%%%%%%%%%% set font size redefine
%\renewcommand{\Large}{\fontsize{16}{22}\selectfont}

\renewcommand\maketitle{%
	
	%% clear page numbering
	\thispagestyle{empty}
	\pagestyle{empty}
	
	\begin{titlepage}
		\begin{flushleft}
			{\Huge \textbf{การเรียนรู้เชิงสถิติสำหรับปัญญาประดิษฐ์}}\\
					\vspace{0.5cm}	
			{\LARGE  \textbf{Statistical Learning for Artificial Intelligence}}
		\end{flushleft}
		\vspace{20cm}   %default \vspace{6.9cm}
		\begin{flushright}
			{\LARGE  \textbf{พัชรี\hspace{0.2cm}มณีรัตน์}}
		\end{flushright}
		\cleardoublepage
	\end{titlepage}%
	
	
	\begin{titlepage}
		\begin{flushleft}
			{\Huge \textbf{การเรียนรู้เชิงสถิติสำหรับปัญญาประดิษฐ์}}\\
			\vspace{0.5cm}	
			{\LARGE  \textbf{Statistical Learning for Artificial Intelligence}}
		\end{flushleft}
		\vspace{5cm}
		\begin{flushleft}
			{\Huge \textbf{พัชรี\hspace{0.2cm}มณีรัตน์}}\\
			\vspace{0.5cm}
			{\Large\textbf{มหาวิทยาลัยราชภัฏอุตรดิตถ์}}
		\end{flushleft}
		\vspace{6cm}
		\begin{flushleft}
			{\Large \textbf{ข้อมูลทางบรรณานุกรม:}} \\
			{\large การเรียนรู้เชิงสถิติสำหรับปัญญาประดิษฐ์ --.\\
			....pages. }
			%1. Data Analysis 2. Data Visualization. I, Maneerat, P. Title.}
		\end{flushleft}
	
		\vspace{3cm}
		\begin{flushleft}
			{\large \textbf{จัดพิมพ์โดย มหาวิทยาลัยราชภัฏอุตรดิตถ์}}
		\end{flushleft}
		\cleardoublepage
	\end{titlepage}%
	
	
	
	\begin{titlepage}
		\begin{center}
			{\LARGE \textbf{Writor's Note}}
		\end{center}
		\vspace{0.3cm}
		\indent 
		\hspace{0.4cm}
		Dear Reader, \\~\\
		
		
		Welcome to "Data Analytics and Data Visualization: A Comprehensive Guide". In an age where data is often called the new oil, understanding how to refine this raw resource into valuable insights has become an essential skill across industries and disciplines. Whether you're a student, a professional looking to upskill, or a curious mind eager to understand the data-driven world around us, this book is designed to be your companion on the journey through the fascinating realm of data.  \\
		
		
		As I embarked on writing this book, I was driven by a simple yet powerful goal: to demystify the complex world of data analytics and visualization, making it accessible to readers from all backgrounds. Too often, these subjects are shrouded in technical jargon and complex mathematics, intimidating those who could benefit most from understanding them. My aim is to break down these barriers, providing clear explanations, relatable examples, and practical insights that you can apply in your own work or studies.  \\
		
		
		This book is the result of years of experience in the field, countless conversations with professionals and students, and a deep dive into the latest research and technologies. But more than that, it's born from a genuine excitement about the potential of data to transform our understanding of the world and drive positive change.
		As you read through these pages, you'll notice a few key themes:  \\
		
		\begin{enumerate}
			\item	\textbf{From Theory to Practice:} While we cover theoretical concepts, we always tie them back to real-world applications. You'll find case studies, examples, and hands-on exercises throughout the book to help you apply what you've learned.
			
			\item \textbf{Interdisciplinary Approach:} Data does not exist in a vacuum. We explore how data analytics and visualization apply across various fields, from business and science to public policy and social good.
			
			\item \textbf{Ethical Considerations:} As we delve into the power of data, we also critically examine the responsibilities that come with it. Discussions on data privacy, bias, and ethical decision-making are woven throughout the text.
			
			\item \textbf{Future-Focused:} The field of data analytics and visualization is rapidly evolving. While we cover the foundational concepts, we also look ahead to emerging trends and technologies that are shaping the future of the field.
			
			\item \textbf{Accessibility:} Every effort has been made to explain complex concepts in clear, understandable language. You don't need to be a mathematician or a computer scientist to grasp the ideas presented here.
		\end{enumerate}
		
		
		
		Remember, the journey to mastering data analytics and visualization is ongoing. This book is not just a one-time read, but a resource you can return to as you grow in your understanding and application of these concepts.
		I encourage you to approach this book with curiosity and an open mind. Don't hesitate to challenge ideas, ask questions, and most importantly, apply what you learn to your own unique contexts. The true power of data comes not just from understanding it, but from using it to make better decisions, tell compelling stories, and drive meaningful change.  \\
		
		
		Thank you for joining me on this exciting journey. My hope is that by the time you finish this book, you'll not only have a solid grasp of data analytics and visualization but also share my enthusiasm for the endless possibilities they offer. \\
		
		Let's dive in and start exploring the world of data together!
		
		\vspace{2.5cm}
		\begin{minipage}{0.9\textwidth}\raggedleft
			PATCHAREE MANEERAT
		\end{minipage}
	\end{titlepage}











	
}% End \maketitle