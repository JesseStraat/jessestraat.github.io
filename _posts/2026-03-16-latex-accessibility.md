---
layout: post
title: "Accessibility standards in LaTeX"
date: 2026-03-16
last_modified_at: 2026-03-24
categories:
- LaTeX
---

For ages, LaTeX has been largely inaccessible for the visually impaired. The PDFs produced by it simply do not contain the necessary information for a screen reader to work properly. As the [2025 PDF days poster by the LaTeX project](https://pdfa.org/download-area/posters/PDFDaysEurope2025-TechnicalPoster-LaTeX.pdf) phrases it, PDFs are evil. [A 2012 article by the National Federation of the Blind](https://nfb.org/sites/default/files/images/nfb/publications/fr/fr31/2/fr310212.htm) reveals that the classical way for the visually impaired to read a LaTeX document is simply by reading the source code, which, of course, is not always available. Other solutions, such as [one used by arXiv](https://arxiv.org/html/2402.08954v1), convert LaTeX files into accessible formats, though this is incompatible with a lot of packages, since the program must know how to interpret them; doing it properly amounts to rebuilding (La)TeX from the ground up for your output of choice, and keeping up with all new developments.

There is hope on the horizon: with the advent of [PDF/UA-2](https://pdfa.org/iso-14289-2-pdfua-2/), which is part of PDF 2.0, PDFs now have the necessary metadata to directly be converted/read as an accessible document. Recent work by the LaTeX project, known as the [tagging project](https://latex3.github.io/tagging-project/), has made great strides in creating such PDFs using LaTeX. While still in active development, it is already mostly usable. I also believe it is important to spread awareness about these new features, since they are not yet widely adopted; only a few PDF readers actually support it, so we should push for them to implement it.

* Table of contents placeholder
{:toc}

# Solving PDF inaccessibility

The three main issues in accessibility of a LaTeX document (or more generally, any PDF) are

1. Images aren't accompanied by an alt text, which describe the image's contents.
2. Other odd visual structures, such as tables and lists, don't have any metadata explaining the structure, so a computer can only guess at what it looks like.
3. The maths is often purely visual; there is no underlying metadata about the meaning of a formula. Any attempts by screen readers to read them aloud leads to pure gibberish.

To see how other file formats solve these issues, we shall consider HTML, which is well-known for its accessibility. Below is an example of what an HTML file might look like.
```html
<html>
    <h1>This is a heading</h1>
    <p>This is a paragraph, and
        <i>this is in italics</i>
    </p>
    <figure>
        Here could be some figure
    </figure>
    <ul>
        <li> A list item.</li>
        <li> Another list item.</li>
    </ul>
    <table>
        <caption>This is a table</caption>
        <tr>
            <th>First row, first column and header</th>
            <th>First row, second column and header</th>
        </tr>
        <tr>
            <td>Second row, first column</td>
            <td>Second row, second column</td>
        </tr>
    </table>
</html>
```
The bracketed objects are known as *tags*. It is then up to the interpreter, i.e., your browser, to interpret the meaning of these tags and display the HTML. This is completely different from how a PDF works: it has static visuals that leave very little up to interpretation.

Maths in HTML can be approached by using [MathML](https://en.wikipedia.org/wiki/MathML). It again works by using tags. For example, \\(a^2 + b^2 = c^2\\) is written in MathML as below.
```html
<math xmlns="http://www.w3.org/1998/Math/MathML">
    <msup>
        <mi>a</mi><mn>2</mn>
    </msup>
    <mo>+</mo>
    <msup>
        <mi>b</mi><mn>2</mn>
    </msup>
    <mo>=</mo>
    <msup>
        <mi>c</mi><mn>2</mn>
    </msup>
</math>
```
PDF/UA-2 works largely in very much the same way as HTML does, by providing a *structure tree*. This is a collection of tags which are embedded into one another. We consider the following example.
```LaTeX
\documentclass{article}
\usepackage{graphicx}

\begin{document}
    \section{Foo}
    %
    This is a paragraph and \emph{this is in italics}
    \begin{figure}
        \centering
        \includegraphics[width=0.5\textwidth]{example-image-a}
        \caption{Here could be some figure}
    \end{figure}
    \begin{itemize}
        \item A list item.
        \item Another list item.
    \end{itemize}
    \begin{table}
        \centering
        \caption{This is a table}
        \begin{tabular}{ c | c }
            First row, first column and header & First row, second column and header\\\hline
            Second row, first column & Second row, second column
        \end{tabular}
    \end{table}
    \begin{equation}
        a^2 + b^2 = c^2
    \end{equation}
\end{document}
```
When set up correctly, and after converting to XML using `show-pdf-tags` (see [“Seeing PDF tags”](#seeing-pdf-tags)), we find the following structure tree (I've heavily trimmed it down; for the full set-up LaTeX file and XML output, refer to [the final section](#a-full-example)).
```xml
<PDF>
   <StructTreeRoot>
      <Document>
         <Sect>
            <section title="Foo">
               Foo
            </section>
            <text>
               This is a paragraph and <Em>this is in italics</Em>
            </text>
            <itemize>
               <LI>
                  <text>A list item.</text>
               </LI>
               <LI>
                  <text>Another list item.</text>
               </LI>
            </itemize>
            <Formula>
               <math xmlns="http://www.w3.org/1998/Math/MathML">
                  <Lbl>(1)</Lbl>
                  <msup>
                     <mi>a</mi><mn>2</mn>
                  </msup>
                  <mo>+</mo>
                  <msup>
                     <mi>b</mi><mn>2</mn>
                  </msup>
                  <mo>=</mo>
                  <msup>
                     <mi>c</mi><mn>2</mn>
                  </msup>
               </math>
            </Formula>
         </Sect>
         <figures>
            <Caption>
               <Lbl>Figure 1: </Lbl>
               <text>Here could be some figure</text>
            </Caption>
            <Figure 
               alt="An image with the letter &quot;A&quot;."
            >
            </Figure>
         </figures>
         <tables>
            <Caption>
               <Lbl>Table 1: </Lbl>
               <text>This is a table</text>
            </Caption>
            <Table>
               <TR>
                  <TH>First row, first column and header</TH>
                  <TH>First row, second column and header</TH>
               </TR>
               <TR>
                  <TD>Second row, first column</TD>
                  <TD>Second row, second column</TD>
               </TR>
            </Table>
         </tables>
      </Document>
   </StructTreeRoot>
</PDF>
```
Note that this example was highly simplified, and a lot of information was removed. Note also the high similarity to the HTML examples above. One might say that PDF is made accessible by including another HTML-like file standard *within* the PDF. This also makes it possible to canonically [convert a PDF to HTML](https://pdfa.org/resource/deriving-html-from-pdf/), as implemented by, for example, [NGPDF](https://ngpdf.com). This immediately makes it possible to use all (accessibility) tools developed for HTML.

Beyond just accessibility, there are other amazing features made possible by tags. First, by using the structure tree, it is possible to resize the text to fit a screen. This is particularly useful for reading text on mobile devices, since narrow text is easier to read than the wide text common in PDFs. Another advantage is that readers can recognise tagged tables. Copy-pasting a table from a PDF to a spreadsheet program such as Excel would then preserve the layout. This would make data entry from papers much easier.

# Implementing the tagging project in practice
Official information on the implementation can be found on [the website of the tagging project](https://latex3.github.io/tagging-project/documentation/usage-instructions).

To enable tagging, one adds the following code to the beginning of your LaTeX file (even before the documentclass).
```LaTeX
\DocumentMetadata{
   lang        = en,
   pdfstandard = ua-2,
   pdfstandard = a-4f,
   tagging=on,
   tagging-setup={math/setup=mathml-SE} 
}
```
Tagging is only supported for pdfLaTeX and LuaLaTeX. However, the authors, and I, highly advise to use LuaLaTeX, since it is necessary for some maths functionality.

Tagging is only available for some document classes. These include, but are not limited to, the following classes and their derivatives:
- `article`,
- `book`,
- `report`.

In particular, tagging is incompatible with the following classes and their derivatives:
- `beamer`,
- `letter` (partially),
- `novel`,
- `standalone`.

Most tagging is then performed automatically. For some things, however, one should make some manual adjustments. These are outlined below.

For general accessibility guidelines, one may refer to, for example [Wikipedia's](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Accessibility) or [Cambridge University Press's](https://www.cambridge.org/authorhub/application/files/3417/5344/8763/6738_A4_Accessibility_Proof1.pdf). Links and colours, in particular, are not covered by the tagging project, and should be adapted manually.

## Formulas
To generate MathML code, it is necessary to use LuaLaTeX. Furthermore, while strictly not required, it is highly recommended to use the `unicode-math` package. Without it, a lot of maths will not translate to MathML correctly. It does introduce some incompatibilities; more about that in [“What's lost”](#whats-lost). Beyond this, the process is automatic.

## Images
Images must be supplied with an alt-text. The alt-text replaces the image, and should describe its content. Generally, it's different from the caption. A good rule of thumb is that a reader should understand the image from reading just the alt-text. For more information on alt-texts, one may refer to the [Wikipedia help page](https://en.wikipedia.org/wiki/Help:Alt_text).

To add alt-text, one uses the `alt={text goes here}` optional parameter in `\includegraphics`, `\tikz`, `\begin{tikzpicture}` or `\begin{picture}`. For example,
```LaTeX
\begin{figure}
   \centering
   \includegraphics[alt={The LaTeX project logo.}]{latexproject.pdf}
   \caption{An example of a logo.}
\end{figure}
\begin{figure}
   \centering
   \begin{tikzpicture}[alt={A drawing of a duck wearing a cape}]
      \duck[cape]
   \end{tikzpicture}
   \caption{An image of a duck.}
\end{figure}
```

Alternatively, an image without any inherent meaning (such as a background) must be tagged as an artifact (see also the [“Artifacts”](#artifacts) section below). This makes sure it doesn't appear in the structure tree at all, and will be ignored by screen readers. It's implemented by using the `artifact` optional parameter, e.g.,
```LaTeX
\includegraphics[artifact]{background.jpg}
\begin{tikzpicture}[artifact]
   \node at (0,0) {Ignore this};
\end{tikzpicture}
```

## Tables
Tables are tagged automatically. However, for proper accessibility, it is necessary to tell LaTeX which rows function as *headers*, as opposed to ordinary cells. For this, one uses `\tagpdfsetup`.
```LaTeX
\tagpdfsetup{table/header-rows={1}}
\begin{tabular}{ c | c }
   \(x\) & \(f(x)\)\\\hline
   \(0\) & \(0\)\\
   \(1\) & \(2\)\\
   \(2\) & \(9\)
\end{tabular}
```
The above code makes the first row a header, and all other rows ordinary cells. It's also possible to use a comma-separated list as header rows, e.g., `\tagpdfsetup{table/header-rows={1,2,4}}`, which makes the first, second and fourth rows headers.

If you want to use a table for alignment, i.e., it shouldn't be labeled as a table, instead use `\tagpdfsetup{table/tagging=presentation}`.

## Lists
Lists are tagged fully automatically, but have been implemented differently from ordinary LaTeX. This includes the option to start an `enumerate` environment at a different number, or resume counting from the previous `enumerate`. This is then tagged automatically, too. An example is below.
```LaTeX
\begin{enumerate}[start=11]
   \item Item 11
   \item Item 12
\end{enumerate}
Bla bla filler text.
\begin{enumerate}[resume=true]
   \item Item 13
   \item Item 14
\end{enumerate}
```
As usual, it remains possible to embed lists in one another.

## Artifacts
An artifact is a special type of tag that isn't part of the structure tree, at all. They are used to tag pieces of meaningless content, such as decorations, page layout or fillers. Using artifacts in the right places is just as important as tagging. Consider, for example, the following common style of table of contents:
```
1. Introduction.....................................................3
2. Methods..........................................................6
```
If the dots aren't tagged as artifacts, a screen reader will read them out, which takes away from the flow of the document. Ordinary end users should realistically only have to tag images as artifacts, which has been described above in the [“Images”](#images) section. However, if one (especially as a package author) wants to label something as an artifact, it can be done as follows,
```LaTeX
Introduction
\tagmcbegin{artifact}
.....................................................
\tagmcend
3
```
More information can be found in the [`tagpdf` documentation](https://ctan.org/pkg/tagpdf). I urge package authors to read it.

# Seeing PDF structure trees
Both MiKTeX and TeX Live ship with `show-pdf-tags.lua`. This script makes it possible to display the structure tree of any PDF. Simply run `show-pdf-tags --xml [file location]` in your command prompt, and it should show you the tags in XML format.

Some PDF viewers are also able to display the structure tree. The only major PDF readers that support this (as of writing) are Adobe Acrobat and Foxit. For both of these, however, it's a paid feature! In my opinion, this is ridiculous, since it's an essential feature for making document accessible. There are some free (though closed-source) PDF viewers that have the feature, as well, but I can't vouch for them. Currently, `show-pdf-tags` is the best solution.

# What's lost
The big disadvantage of the tagging project is its incompatibility with some widely-used packages. Full information on compatibility can be found on [the tagging project website](https://latex3.github.io/tagging-project/tagging-status/).

The biggest incompability in my testing is that `unicode-math` is incompatible with `amssymb` and other common packages which include maths symbols. Examples of these symbols are `\mathbb{...}`, `\mathscr{...}`, etc., but also objects such as `\lVert`. For technical reasons, it overwrites these macros, and displays them as Unicode text instead of fancy-looking ASCII. For example, `\mathbb{Z}` literally becomes “ℤ”, while `amssymb` would just have it become the letter “Z” with fancy visuals. What ℤ then looks like is fully determined by the font you've selected. While nothing changes *functionally* — your documents will compile all the same — visually, the mathematical fonts we mathematicians have been used to for decades are changed drastically. In particular, `\mathscr` becomes a synonym for `\mathcal`. I believe the benefits outweigh the losses. Beyond just the tagging project, Unicode also makes it possible to look up maths in a document. In my opinion, the AMS fonts are heavily outdated, and it's good that we're moving away from them (though it would be nice if we had a font that changed the visuals of `unicode-math` to that of `amssymb`).

The AMS packages may also produce some issues with tagging. This particularly happens in equations and theorems. However, solving these issues is a high priority of the tagging project, so most issues are patched in no time. Currently, ordinary use should not produce any significant errors.

Speaking of theorems, `thmtools` is incompatible. The numbering is simply wrong. This is also high priority, so it might be fixed in the future.

`tikz-cd` is incompatible. Using it will throw errors.

For those still using it (you shouldn't!!!), `physics` will not be supported. It's likely that some of its functionalities produce errors.

Macros such as `\textbf` and `\bfseries` aren't supported in regular text. Instead, one should use `\emph` to emphasise text. Even outside the tagging project, it's advised to use `\emph` for more consistent documents.

Beyond these, I have not (yet) run into any incompatibilities with the packages that I regularly use.

# The future of PDF accessibility
I think it's clear that accessibility is something to strive for, but we're far from it being universally applied (and, to be fair, the project is still in development). In [(Pierrès et al., 2024)](https://doi.org/10.1007/978-3-031-62846-7_5), we read that almost all academic publications aren't nearly accessible enough. To change this, it is important we spread awareness of these standards, the new tools, and their current poor implementation. Furthermore, at least in my case, most of my LaTeX documents are unpublished, so we should also keep ourselves accountable and make those accessible, too.

As LaTeX developers, we should also consider how accessible our packages are. Are they compatible with the tagging project and `unicode-math`? Do the macros produce meaningful text, or are they images disguised as text without any meaningful Unicode? Do the images produced have meaningful alt-texts? Should a piece of code that's purely for the document layout be tagged as an artifact?

# A full example
Here is the full, tagged example of the above LaTeX file. First is the LaTeX code.
{% include codeblock_with_download.html filepath="latex_accessibility/example.tex" lang="LaTeX" %}
This leads to the following XML.
```xml
<PDF>
 <StructTreeRoot>
  <Document xmlns="http://iso.org/pdf2/ssn"
     id="ID.002"
    >
   <Sect xmlns="http://iso.org/pdf2/ssn"
      id="ID.005"
     >
    <section xmlns="https://www.latex-project.org/ns/dflt"
       id="ID.006"
       title="Foo"
       rolemaps-to="H1"
      >
     <section-number xmlns="https://www.latex-project.org/ns/dflt"
        id="ID.007"
        rolemaps-to="Span"
       >
      <?MarkedContent page="1" ?>1 
     </section-number>
     <?MarkedContent page="1" ?>Foo
    </section>
    <text-unit xmlns="https://www.latex-project.org/ns/dflt"
       id="ID.008"
       rolemaps-to="Part"
      >
     <text xmlns="https://www.latex-project.org/ns/dflt"
        id="ID.009"
        xmlns:Layout="http://iso.org/pdf/ssn/Layout"
        Layout:TextAlign="Justify"
        rolemaps-to="P"
       >
      <?MarkedContent page="1" ?>This is a paragraph and 
      <Em xmlns="http://iso.org/pdf2/ssn"
         id="ID.010"
        >
       <?MarkedContent page="1" ?>this is in italics
      </Em>
      <?MarkedContent page="1" ?> 
     </text>
     <itemize xmlns="https://www.latex-project.org/ns/dflt"
        id="ID.018"
        xmlns:List="http://iso.org/pdf/ssn/List"
        List:ListNumbering="Unordered"
        rolemaps-to="L"
       >
      <LI xmlns="http://iso.org/pdf2/ssn"
         id="ID.019"
        >
       <Lbl xmlns="http://iso.org/pdf2/ssn"
          id="ID.020"
         >
        <?MarkedContent page="1" ?>•
       </Lbl>
       <LBody xmlns="http://iso.org/pdf2/ssn"
          id="ID.021"
         >
        <text-unit xmlns="https://www.latex-project.org/ns/dflt"
           id="ID.022"
           rolemaps-to="Part"
          >
         <text xmlns="https://www.latex-project.org/ns/dflt"
            id="ID.023"
            xmlns:Layout="http://iso.org/pdf/ssn/Layout"
            Layout:TextAlign="Justify"
            rolemaps-to="P"
           >
          <?MarkedContent page="1" ?>A list item.
         </text>
        </text-unit>
       </LBody>
      </LI>
      <LI xmlns="http://iso.org/pdf2/ssn"
         id="ID.024"
        >
       <Lbl xmlns="http://iso.org/pdf2/ssn"
          id="ID.025"
         >
        <?MarkedContent page="1" ?>•
       </Lbl>
       <LBody xmlns="http://iso.org/pdf2/ssn"
          id="ID.026"
         >
        <text-unit xmlns="https://www.latex-project.org/ns/dflt"
           id="ID.027"
           rolemaps-to="Part"
          >
         <text xmlns="https://www.latex-project.org/ns/dflt"
            id="ID.028"
            xmlns:Layout="http://iso.org/pdf/ssn/Layout"
            Layout:TextAlign="Justify"
            rolemaps-to="P"
           >
          <?MarkedContent page="1" ?>Another list item.
         </text>
        </text-unit>
       </LBody>
      </LI>
     </itemize>
    </text-unit>
    <text-unit xmlns="https://www.latex-project.org/ns/dflt"
       id="ID.043"
       rolemaps-to="Part"
      >
     <Formula xmlns="http://iso.org/pdf2/ssn"
        id="ID.044"
        title="equation"
        xmlns:Layout="http://iso.org/pdf/ssn/Layout"
        Layout:Placement="Block"
       >
      <math xmlns="http://www.w3.org/1998/Math/MathML"
         id="ID.047"
         display="block"
        >
       <mtable xmlns="http://www.w3.org/1998/Math/MathML"
          id="ID.048"
          displaystyle="true"
         >
        <mtr xmlns="http://www.w3.org/1998/Math/MathML"
           id="ID.049"
          >
         <mtd xmlns="http://www.w3.org/1998/Math/MathML"
            id="ID.050"
            intent=":equation-label"
           >
          <mtext xmlns="http://www.w3.org/1998/Math/MathML"
             id="ID.045"
            >
           <Lbl xmlns="http://iso.org/pdf2/ssn"
              id="ID.046"
             >
            <?MarkedContent page="1" ?>(1)
           </Lbl>
          </mtext>
         </mtd>
         <mtd xmlns="http://www.w3.org/1998/Math/MathML"
            id="ID.051"
            intent=":pause-medium"
           >
          <mrow xmlns="http://www.w3.org/1998/Math/MathML"
             id="ID.052"
            >
          </mrow>
          <msup xmlns="http://www.w3.org/1998/Math/MathML"
             id="ID.053"
            >
           <mi xmlns="http://www.w3.org/1998/Math/MathML"
              id="ID.054"
             >
            <?MarkedContent page="1" ?>𝑎
           </mi>
           <mn xmlns="http://www.w3.org/1998/Math/MathML"
              id="ID.055"
             >
            <?MarkedContent page="1" ?>2
           </mn>
          </msup>
          <mo xmlns="http://www.w3.org/1998/Math/MathML"
             id="ID.056"
             lspace="0.222em"
             rspace="0.222em"
            >
           <?MarkedContent page="1" ?>+
          </mo>
          <msup xmlns="http://www.w3.org/1998/Math/MathML"
             id="ID.057"
            >
           <mi xmlns="http://www.w3.org/1998/Math/MathML"
              id="ID.058"
             >
            <?MarkedContent page="1" ?>𝑏
           </mi>
           <mn xmlns="http://www.w3.org/1998/Math/MathML"
              id="ID.059"
             >
            <?MarkedContent page="1" ?>2
           </mn>
          </msup>
          <mo xmlns="http://www.w3.org/1998/Math/MathML"
             id="ID.060"
             lspace="0.278em"
             rspace="0.278em"
            >
           <?MarkedContent page="1" ?>=
          </mo>
          <msup xmlns="http://www.w3.org/1998/Math/MathML"
             id="ID.061"
            >
           <mi xmlns="http://www.w3.org/1998/Math/MathML"
              id="ID.062"
             >
            <?MarkedContent page="1" ?>𝑐
           </mi>
           <mn xmlns="http://www.w3.org/1998/Math/MathML"
              id="ID.063"
             >
            <?MarkedContent page="1" ?>2
           </mn>
          </msup>
         </mtd>
        </mtr>
       </mtable>
      </math>
     </Formula>
    </text-unit>
   </Sect>
   <figures xmlns="https://www.latex-project.org/ns/dflt"
      id="ID.003"
      rolemaps-to="Sect"
     >
    <float xmlns="https://www.latex-project.org/ns/dflt"
       id="ID.011"
       rolemaps-to="Aside"
      >
     <Caption xmlns="http://iso.org/pdf2/ssn"
        id="ID.015"
       >
      <Lbl xmlns="http://iso.org/pdf2/ssn"
         id="ID.016"
        >
       <?MarkedContent page="1" ?>Figure 1: 
      </Lbl>
      <text xmlns="https://www.latex-project.org/ns/dflt"
         id="ID.017"
         xmlns:Layout="http://iso.org/pdf/ssn/Layout"
         Layout:TextAlign="Center"
         rolemaps-to="P"
        >
       <?MarkedContent page="1" ?>Here could be some figure
      </text>
     </Caption>
     <text-unit xmlns="https://www.latex-project.org/ns/dflt"
        id="ID.012"
        rolemaps-to="Part"
       >
      <text xmlns="https://www.latex-project.org/ns/dflt"
         id="ID.013"
         xmlns:Layout="http://iso.org/pdf/ssn/Layout"
         Layout:TextAlign="Center"
         rolemaps-to="P"
        >
       <Figure xmlns="http://iso.org/pdf2/ssn"
          id="ID.014"
          alt="An image with the letter &quot;A&quot;."
          xmlns:Layout="http://iso.org/pdf/ssn/Layout"
          Layout:BBox="{ 219.69614, 538.30307, 391.55169, 667.19801 }"
         >
        <?MarkedContent page="1" ?>
       </Figure>
      </text>
     </text-unit>
    </float>
   </figures>
   <tables xmlns="https://www.latex-project.org/ns/dflt"
      id="ID.004"
      rolemaps-to="Sect"
     >
    <float xmlns="https://www.latex-project.org/ns/dflt"
       id="ID.029"
       rolemaps-to="Aside"
      >
     <Caption xmlns="http://iso.org/pdf2/ssn"
        id="ID.030"
       >
      <Lbl xmlns="http://iso.org/pdf2/ssn"
         id="ID.031"
        >
       <?MarkedContent page="1" ?>Table 1: 
      </Lbl>
      <text xmlns="https://www.latex-project.org/ns/dflt"
         id="ID.032"
         xmlns:Layout="http://iso.org/pdf/ssn/Layout"
         Layout:TextAlign="Center"
         rolemaps-to="P"
        >
       <?MarkedContent page="1" ?>This is a table
      </text>
     </Caption>
     <text-unit xmlns="https://www.latex-project.org/ns/dflt"
        id="ID.033"
        rolemaps-to="Part"
       >
      <text xmlns="https://www.latex-project.org/ns/dflt"
         id="ID.034"
         xmlns:Layout="http://iso.org/pdf/ssn/Layout"
         Layout:TextAlign="Center"
         rolemaps-to="P"
        >
      </text>
      <Table xmlns="http://iso.org/pdf2/ssn"
         id="ID.035"
        >
       <TR xmlns="http://iso.org/pdf2/ssn"
          id="ID.036"
         >
        <TH xmlns="http://iso.org/pdf2/ssn"
           id="ID.037"
           xmlns:Table="http://iso.org/pdf/ssn/Table"
           Table:Scope="Column"
          >
         <?MarkedContent page="1" ?>First row, first column and header
        </TH>
        <TH xmlns="http://iso.org/pdf2/ssn"
           id="ID.038"
           xmlns:Table="http://iso.org/pdf/ssn/Table"
           Table:Scope="Column"
          >
         <?MarkedContent page="1" ?>First row, second column and header
        </TH>
       </TR>
       <TR xmlns="http://iso.org/pdf2/ssn"
          id="ID.039"
         >
        <TD xmlns="http://iso.org/pdf2/ssn"
           id="ID.040"
          >
         <?MarkedContent page="1" ?>Second row, first column
        </TD>
        <TD xmlns="http://iso.org/pdf2/ssn"
           id="ID.041"
          >
         <?MarkedContent page="1" ?>Second row, second column
        </TD>
       </TR>
      </Table>
      <text xmlns="https://www.latex-project.org/ns/dflt"
         id="ID.042"
         rolemaps-to="P"
        >
      </text>
     </text-unit>
    </float>
   </tables>
  </Document>
 </StructTreeRoot>
</PDF>
```