# revision 21326
# category Package
# catalog-ctan /fonts/fonetika
# catalog-date 2008-08-19 20:38:14 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-fonetika
Version:	20080819
Release:	3
Summary:	Support for the danish "Dania" phonetic system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fonetika
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonetika.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonetika.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Fonetika Dania is a font bundle with a serif font and a sans
serif font for the danish phonetic system Dania. Both fonts
exist in regular and bold weights. LaTeX support is provided.
The fonts are based on URW Palladio and Iwona Condensed, and
were created using FontForge.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/fonetika/FonetikaDaniaIwonaeBold.afm
%{_texmfdistdir}/fonts/afm/public/fonetika/FonetikaDaniaIwonaeRegular.afm
%{_texmfdistdir}/fonts/afm/public/fonetika/FonetikaDaniaPallaeBold.afm
%{_texmfdistdir}/fonts/afm/public/fonetika/FonetikaDaniaPallaeRegular.afm
%{_texmfdistdir}/fonts/map/dvips/fonetika/fonetika.map
%{_texmfdistdir}/fonts/tfm/public/fonetika/fonetika.tfm
%{_texmfdistdir}/fonts/tfm/public/fonetika/fonetikabold.tfm
%{_texmfdistdir}/fonts/tfm/public/fonetika/fonetikasans.tfm
%{_texmfdistdir}/fonts/tfm/public/fonetika/fonetikasansbold.tfm
%{_texmfdistdir}/fonts/truetype/public/fonetika/FonetikaDaniaIwonaeBold.ttf
%{_texmfdistdir}/fonts/truetype/public/fonetika/FonetikaDaniaIwonaeRegular.ttf
%{_texmfdistdir}/fonts/truetype/public/fonetika/FonetikaDaniaPallaeBold.ttf
%{_texmfdistdir}/fonts/truetype/public/fonetika/FonetikaDaniaPallaeRegular.ttf
%{_texmfdistdir}/fonts/type1/public/fonetika/FonetikaDaniaIwonaeBold.pfb
%{_texmfdistdir}/fonts/type1/public/fonetika/FonetikaDaniaIwonaeRegular.pfb
%{_texmfdistdir}/fonts/type1/public/fonetika/FonetikaDaniaPallaeBold.pfb
%{_texmfdistdir}/fonts/type1/public/fonetika/FonetikaDaniaPallaeRegular.pfb
%{_texmfdistdir}/tex/latex/fonetika/fonetika.sty
%{_texmfdistdir}/tex/latex/fonetika/t1fonetika.fd
%doc %{_texmfdistdir}/doc/fonts/fonetika/README
%doc %{_texmfdistdir}/doc/fonts/fonetika/fonetika.pdf
%doc %{_texmfdistdir}/doc/fonts/fonetika/fonetika.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080819-2
+ Revision: 752007
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080819-1
+ Revision: 718477
- texlive-fonetika
- texlive-fonetika
- texlive-fonetika
- texlive-fonetika

