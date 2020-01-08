Summary:	GNOME Klotski
Summary(pl.UTF-8):	Klotski dla GNOME
Name:		gnome-klotski
Version:	3.34.3
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-klotski/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	73b65abc7396dca95ef973c1c37ca177
URL:		https://wiki.gnome.org/Apps/Klotski
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	libgnome-games-support-devel >= 1.0
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.27.1
BuildRequires:	vala-libgee >= 0.8
BuildRequires:	vala-librsvg >= 2.32.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.20.0
Requires:	hicolor-icon-theme
Requires:	libgnome-games-support >= 1.0
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%{_datadir}/glib-2.0/schemas/org.gnome.Klotski.gschema.xml
%{_datadir}/metainfo/org.gnome.Klotski.appdata.xml
%{_desktopdir}/org.gnome.Klotski.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Klotski.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Klotski.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Klotski-symbolic.svg
%{_mandir}/man6/gnome-klotski.6*
