%global tl_name fonetika
%global tl_revision 21326

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for the Danish Dania phonetic system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fonetika
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonetika.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonetika.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Fonetika Dania is a font bundle with a serif font and a sans serif font
for the danish phonetic system Dania. Both fonts exist in regular and
bold weights. LaTeX support is provided. The fonts are based on URW
Palladio and Iwona Condensed, and were created using FontForge.

