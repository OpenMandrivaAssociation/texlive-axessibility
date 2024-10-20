Name:		texlive-axessibility
Version:	57105
Release:	2
Summary:	Access to formulas in PDF files by assistive technologies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/axessibility
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/axessibility.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/axessibility.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/axessibility.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
PDF documents containing formulas generated by LaTeX are
usually not accessible by assistive technologies for visually
impaired people and people with special educational needs
(i.e., by screen readers and braille displays). The
axessibility package manages this issue, allowing to create a
PDF document where the formulas are read by these assistive
technologies, since it automatically generates hidden comments
in the PDF document (by means of the /ActualText attribute
and/or suitable tags) in correspondence to each formula.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/axessibility
%{_texmfdistdir}/tex/latex/axessibility
%doc %{_texmfdistdir}/doc/latex/axessibility

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
