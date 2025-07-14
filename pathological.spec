Summary:	A puzzle game involving paths and marbles
Summary(pl.UTF-8):	Układanka ze ścieżkami i kafelkami
Name:		pathological
Version:	1.1.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/pathological/%{name}-%{version}.tar.gz
# Source0-md5:	76a446080c0fed12baf39354d8e0ce4a
Source1:	%{name}.desktop
Patch0:		%{name}-datadir.patch
URL:		http://pathological.sourceforge.net/
Requires:	python-pygame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pathological is an enriched clone of the game "Logical" by Rainbow
Arts. To solve a level, fill each wheel with four marbles of matching
color. Various board elements such as teleporters, switches, filters,
etc., make the game interesting and challenging. New levels can be
created using your favorite text editor.

%description -l pl.UTF-8
Pathological to wzbogacony klon gry "Logical" firmy Rainbow Arts. Aby
rozwiązać poziom, należy wypełnić każde koło czterema kafelkami w
pasującym kolorze. Różne elementy planszy, takie jak teleporty,
przełączniki, filtry itp. czynią grę interesującą i wyzywającą. Można
tworzyć nowe poziomy przy użyciu ulubionego edytora tekstu.

%prep
%setup -q
%patch -P0 -p1

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o write-highscores write-highscores.c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_libdir}/%{name}/bin} \
	   $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_mandir}/man6} \
	   $RPM_BUILD_ROOT/var/games

cp -r circuits graphics music sounds $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
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
%dir %{_libdir}/%{name}/bin
%attr(2755,root,games) %{_libdir}/%{name}/bin/write-highscores
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/%{name}.py
%{_datadir}/%{name}/circuits
%{_datadir}/%{name}/graphics
%{_datadir}/%{name}/music
%{_datadir}/%{name}/sounds
%{_desktopdir}/%{name}.desktop
%{_mandir}/man6/*
%{_pixmapsdir}/*
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/pathological_scores
