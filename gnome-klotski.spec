Summary:	GNOME Klotski
Summary(pl.UTF-8):	Klotski dla GNOME
Name:		gnome-klotski
Version:	3.18.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-klotski/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	2f80f35549f41a990e0faea39d8f78d6
URL:		https://wiki.gnome.org/Apps/Klotski
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.15.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.27.1
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.15.0
Requires:	hicolor-icon-theme
Requires:	librsvg >= 2.32.0
Provides:	gnome-games-gnotski = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnotski < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clone of the Klotski game. The objective is to move the patterned
block to the area bordered by green markers.

%description -l pl.UTF-8
Klon gry Klotski. Celem gry jest przesunięcie zaznaczonego klocka w
pole ograniczone zielonymi znacznikami.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-klotski
%{_datadir}/appdata/gnome-klotski.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.klotski.gschema.xml
%{_datadir}/gnome-klotski
%{_desktopdir}/gnome-klotski.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-klotski.png
%{_iconsdir}/hicolor/scalable/apps/gnome-klotski.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-klotski-symbolic.svg
%{_mandir}/man6/gnome-klotski.6*
