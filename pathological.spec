Summary:	A puzzle game involving paths and marbles
Name:		pathological
Version:	1.1.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Icon:		pathological.xpm
Source0:	http://dl.sourceforge.net/%{name}/%{name}_%{version}.tar.gz
# Source0-md5:	40091e7c3a391a52f6b6806770ab944f
Patch0:		%{name}-bash_not_sh.patch
URL:		http://pathological.sourceforge.net/
Requires:	python-pygame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pathological is an enriched clone of the game "Logical" by Rainbow
Arts. To solve a level, fill each wheel with four marbles of matching
color. Various board elements such as teleporters, switches, filters,
etc., make the game interesting and challenging. New levels can be
created using your favorite text editor.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__cc} %{rpmcflags} %{rpmldflags} -o write-highscores write-highscores.c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_libdir}/%{name}/bin} \
	   $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_mandir}/man6} \
	   $RPM_BUILD_ROOT/var/games

cp -r circuits graphics music sounds $RPM_BUILD_ROOT%{_datadir}/%{name}
install pathological.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install pathological $RPM_BUILD_ROOT%{_bindir}
install write-highscores $RPM_BUILD_ROOT%{_libdir}/%{name}/bin
install pathological.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install pathological_scores $RPM_BUILD_ROOT/var/games
install pathological.6* $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO html
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(4755,root,games) %{_libdir}/%{name}/bin/write-highscores
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/%{name}.py
%{_datadir}/%{name}/circuits
%{_datadir}/%{name}/graphics
%{_datadir}/%{name}/music
%{_datadir}/%{name}/sounds
%{_mandir}/man6/*
%{_pixmapsdir}/*
%attr(664,root,games) %config(noreplace) %verify(not md5 size mtime) /var/games/pathological_scores
