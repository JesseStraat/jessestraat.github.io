---
layout: post
title: "Tree-level Gromov–Witten invariants of projective space"
date: 2025-04-30
categories: "appendices"
---

I am currently writing my master's thesis on Gromov--Witten invariants \\(GW_{g,n,\beta}^X(\gamma_1\otimes\cdots\otimes\gamma_n)\\). They roughly correspond to the number of genus \\(g\\) holomorphic curves in a projective variety \\(X\\) that map to a \\(\beta\in H_2(X;\mathbb{Z})\\), together with \\(n\\) marked points such that the \\(i\\)-th marked point passes through the rational cohomology class \\(\gamma_i\\). Thanks to the mapping to a point and divisor axioms (Kontsevich--Manin, 1994), it is possible to simplify the calculation of Gromov--Witten invariants to some countable set of rational numbers
$$\begin{equation}
    GW_{g,n,\beta}^X(q_1^{\otimes n_1}\otimes\cdots\otimes q_D^{\otimes n_D}) = \prod_{i=1}^r \langle q_i,\beta\rangle^{n_i} N_g(n_{r+2},\dots,n_D;\beta).
\end{equation}$$
Here, \\(\beta\\) is assumed to be nonzero and torsion-free, and \\(q_0\dots,q_D\\) are integral generators of \\(H^*(X;\mathbb{Q})\\) such that \\(q_0=1\\) and \\(q_1,\dots,q_r\\) generate \\(H^2(X;\mathbb{Q})\\).

An important tool in calculating genus zero (tree-level) Gromov--Witten invariants is the Witten--Dijkgraaf--Verlinde--Verlinde (WDVV) equation. It is a differential equation on a generating function of the Gromov--Witten invariants known as the Gromov--Witten potential \\(\Phi(x_0,\dots,x_D)\\), such that, roughly,
\\[\partial_{i_1}\cdots\partial_{i_k}\Phi(0) = \sum_{\beta\in H_2(X;\mathbb{Z})}GW_{0,k,\beta}^X(q_{i_1}\otimes\cdots\otimes q_{i_k}).\\]
The WDVV equation is a method of generating recursive methods. However, it does not directly provide a formula, which makes it challenging to work with. If we then know some initial value of the tree-level Gromov--Witten invariants of \\(X\\), we may we able to calculate all others using the WDVV equation.

### Complex projective space

Consider now \\(X=\mathbb{CP}^n\\), and let \\(q\\) be the standard positive generator of \\(H^*(X;\mathbb{Q})\\), and identify \\(H_2(X;\mathbb{Z})\\) with \\(\mathbb{Z}\\) such that \\(\langle q,1\rangle=1\\). The Gromov--Witten invariants are numbers \\(N_0(k_3,\dots,k_n;d)\\). We already know some initial values:
$$\begin{equation}
    GW_{0,3,0}^X(q^i\otimes q^j\otimes q^k) = \delta_{n,i+j+k},\quad GW_{0,3,1}^X(q^i\otimes q^j\otimes q^k) = \delta_{2n+1,i+j+k},\label{eq:initvals}
\end{equation}$$
the latter of which is found by proving that all such Gromov--Witten invariants are equal to \\(GW_{0,3,1}^X(q\otimes q^n\otimes q^n)\\), which is the number of lines through two points.

#### \\(n=1\\)

First, since \\(3>n\\), we discover that the Gromov--Witten invariants of interest are \\(N_0(d)\\) for \\(d>0\\). By equation \eqref{eq:initvals}, we already know that \\(N_0(1)=1\\). Furthermore, due to the grading axiom, all other \\(N_0(d)\\) are zero, so we are done.

#### \\(n=2\\)

Again, \\(3>n\\), so we want to find \\(N_0(d)\\) for \\(d>0\\) with initial value \\(N_0(1)=1\\). The WDVV equation tells us that
$$\begin{equation}
    N_0(d) = \sum_{k+l=d} k^2lN_0(k)N_0(l)\left[l\binom{3d-4}{3k-2} - k\binom{3d-4}{3k-1}\right],
\end{equation}$$
known as Kontsevich's formula. It is a straightforward formula that, while difficult to calculate by hand, is perfect for numerical calculations (see implementation below). Up to \\(d=8\\), they are given by

{% include /code_snippets/GW_calcs/CP2.md %}

#### \\(n=3\\)

This case is immediately more complicated, since the Gromov--Witten invariants of interest are \\(N_0(n;d)\\): the number of \\(d\\)-fold curves that pass through \\(n\\) points and \\(4d-2n\\) lines.
The following equations hold for \\(n\leq 2d-2\\):
$$\begin{multline}
    N_0(n;d) - 2dN_0(n+1;d) = \sum_{k+l=d}\sum_{a+b=n}\binom{n}{a}\\
    k^2N_0(a;k)N_0(b;l)\left[l\binom{4d-2n-3}{4k-2a-1} - k\binom{4d-2n-3}{4k-2a}\right],\label{eq:cp31}
\end{multline}$$
$$\begin{multline}
    N_0(n+1;d) - dN_0(n+2;d) = \sum_{k+l=d}\sum_{a+b=n}\binom{n}{a}\\
    kN_0(a;k)N_0(b+1;l)\left[l^2\binom{4d-2n-4}{4k-2a-2} - k^2\binom{4d-2n-4}{4k-2a}\right].\label{eq:cp32}
\end{multline}$$
This equation holds for \\(d\geq 2\\) and \\(n\leq 2d-3\\):
$$\begin{multline}
    N_0(n+2;d) = \sum_{k+l=d}\sum_{a+b=n}\binom{n}{a}\left\{2k^2l\binom{4d-2n-5}{4k-2a-2}N_0(a+1;k)N_0(b+1;l)\right.\\
    \left.- k^2N_0(a;k)N_0(b+2;l)\left[k\binom{4d-2n-5}{4k-2a} + l\binom{4d-2n-5}{4k-2a-1}\right]\right\}.\label{eq:cp33}
\end{multline}$$
The initial value in equation \eqref{eq:initvals} is \\(N_0(2;1)=1\\). Inductively, these three equations give us all other invariants. Indeed, let us assume that for some \\(d\geq 1\\) we know \\(N_0(2;d)\\) and \\(N_0(a;k)\\) for all \\(k\lt d\\). By \eqref{eq:cp32} with \\(n=0\\), we find that
$$\begin{equation}
    N_0(1;d) = dN_0(2;d) + \sum_{k+l=d} kN_0(0;k)N_0(1;l)\left[l^2\binom{4d-4}{4k-2} - k^2\binom{4d-4}{4k}\right],
\end{equation}$$
and by \eqref{eq:cp31} with \\(n=0\\),
$$\begin{equation}
    N_0(0;d) - 2dN_0(1;d) = \sum_{k+l=d}k^2N_0(0;k)N_0(0;l)\left[l\binom{4d-3}{4k-1} - k\binom{4d-3}{4k}\right].
\end{equation}$$
Equation \eqref{eq:cp32} then gives all other \\(N_0(n;d)\\). Finally, we complete the induction by using \eqref{eq:cp33} with \\(n=0\\) to find
$$\begin{multline}
    N_0(2;d+1) = \sum_{k+l=d+1}2k^2l\binom{4d-1}{4k-2}N_0(1;k)N_0(1;l)\\
    - k^2N_0(0;k)N_0(2;l)\left[k\binom{4d-1}{4k} + l\binom{4d-1}{4k-1}\right].
\end{multline}$$
This algorithm is even more complicated, but perfectly doable for Python. Up to \\(d=6\\), we find

{% include /code_snippets/GW_calcs/CP3.md %}

### Implementation

Here, I describe the script I used to calculate the Gromov--Witten invariants of \\(\mathbb{CP}^2\\) and \\(\mathbb{CP}^3\\).

#### \\(n=2\\)

{% include codeblock_with_download.html filepath="GW_calcs/CP2.py" lang="python" %}

#### \\(n=3\\)

{% include codeblock_with_download.html filepath="GW_calcs/CP3.py" lang="python" %}