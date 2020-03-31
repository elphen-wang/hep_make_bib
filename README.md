# hep_make_bib
Making bib for latex/tex based on an open access digital library [INSPIRE-HEP](https://inspirehep.net/).

# Introduction
Latex/Tex is a powerful tool for writing documents, we who do high-energy physics research often use it. However, we also often fret about making references. Since inserting references is almost an unavoidable problem, let's make it easy to make bib. I wrote a Python scrip that imported the BeautifulSoup (bs4) and urllib modules (recommended Python3) to achieve this goal. Though INSPIRE-HEP offer three formats bib, it is far from enough for perfectionists (like me :smile:).

Unfortunately, this approach may be upgrade as the old version of the INSPIRE-HEP is phased out by June 2020.

# Instruction
Here is an example of how to use it.

```
# cd /some/place 
# python3 make_bib.py
Please input your keyword...

PRD+neutrino+JUNO+2019

Your are searching:  PRD+neutrino+JUNO+2019
You got  3  result(s)
Index.  0 , ---------->title:  Confronting tridirect CP -symmetry models with neutrino oscillation experiments

%\cite{Ding:2019zhn}
\bibitem{Ding:2019zhn}
  G.~J.~Ding, Y.~F.~Li, J.~Tang and T.~C.~Wang,
  {\it{Confronting tridirect CP -symmetry models with neutrino oscillation experiments}},{\color{blue}\href{https://doi.org/10.1103/PhysRevD.100.055022}{  Phys.\ Rev.\ D {\bf 100}, no. 5, 055022 (2019)  }\href{http://arXiv.org/abs/arXiv:1905.12939}{[arXiv:1905.12939 [hep-ph]]}[\href{http://old.inspirehep.net/record/1737505}{\scriptsize IN\normalsize SPIRE}]}


Index.  1 , ---------->title:  Foraging for dark matter in large volume liquid scintillator neutrino detectors with multiscatter events

%\cite{Bramante:2018tos}
\bibitem{Bramante:2018tos}
  J.~Bramante, B.~Broerman, J.~Kumar, R.~F.~Lang, M.~Pospelov and N.~Raj,
  {\it{Foraging for dark matter in large volume liquid scintillator neutrino detectors with multiscatter events}},{\color{blue}\href{https://doi.org/10.1103/PhysRevD.99.083010}{  Phys.\ Rev.\ D {\bf 99}, no. 8, 083010 (2019)  }\href{http://arXiv.org/abs/arXiv:1812.09325}{[arXiv:1812.09325 [hep-ph]]}[\href{http://old.inspirehep.net/record/1711233}{\scriptsize IN\normalsize SPIRE}]}


Index.  2 , ---------->title:  Constraints on the solar $\Delta m^2$ using Daya Bay and RENO data

%\cite{Seo:2018rrb}
\bibitem{Seo:2018rrb}
  S.~H.~Seo and S.~J.~Parke,
  {\it{Constraints on the solar $\Delta m^2$ using Daya Bay and RENO data}},{\color{blue}\href{https://doi.org/10.1103/PhysRevD.99.033012}{  Phys.\ Rev.\ D {\bf 99}, no. 3, 033012 (2019)  }\href{http://arXiv.org/abs/arXiv:1808.09150}{[arXiv:1808.09150 [hep-ex]]}[\href{http://old.inspirehep.net/record/1691733}{\scriptsize IN\normalsize SPIRE}]}

```

For now, you can copy the corresponding bib into your document.  As you may have noticed, the usage of the key words is exactly the same as the inspire-hep. Don't explain much, please see the picture below. ![example](https://github.com/ElonSteveWang/hep_make_bib/blob/master/example.png) Three hyperlinks are inserted into the highlighted blue text to the home pages of the corresponding online journal, ArXiv and INSPIRE-HEP.


# License

 * [hep_make_bib](https://github.com/ElonSteveWang/hep_make_bib) is available under the terms of the [GNU General Public License, version 2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html).
