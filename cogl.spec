#
# Conditional build
%bcond_without	static_libs	# static libraries
#
Summary:	A library for using 3D graphics hardware to draw pretty pictures
Summary(pl.UTF-8):	Biblioteka do rysowania ładnych obrazków przy użyciu sprzętowej grafiki 3D
Name:		cogl
Version:	1.8.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://source.clutter-project.org/sources/cogl/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	d00d3639c75660d5c6a989ab932e9914
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	gettext-devel >= 0.18.1
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	libdrm-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pango-devel >= 1:1.20
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.4
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel >= 3
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Suggests:	OpenGL
Requires:	cairo >= 1.10
Requires:	glib2 >= 1:2.26.0
Requires:	pango >= 1:1.20
Requires:	xorg-lib-libXcomposite >= 0.4
Requires:	xorg-lib-libXfixes >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cogl is a small open source library for using 3D graphics hardware to
draw pretty pictures. The API departs from the flat state machine
style of OpenGL and is designed to make it easy to write orthogonal
components that can render without stepping on each others toes.

%description -l pl.UTF-8
Cogl to mała biblioteka o otwartych źródłach, pozwalająca na rysowanie
ładnych rysunków przy użyciu sprzętu graficznego 3D. API wywodzi się z
automatu skończonego w stylu OpenGL i zostało tak zaprojektowane, aby
ułatwić pisanie ortogonalnych komponentów, potrafiących renderować bez
przeszkadzania sobie nawzajem.

%package devel
Summary:	Header files for cogl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cogl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.10
Requires:	glib2-devel >= 1:2.26.0
Requires:	gobject-introspection-devel >= 0.9.5
Requires:	libdrm-devel
Requires:	pango-devel >= 1:1.20
Requires:	xorg-lib-libXcomposite-devel >= 0.4
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel >= 3

%description devel
Header files for building and developing applications with cogl.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji z użyciem biblioteki cogl.

%package static
Summary:	Static cogl libraries
Summary(pl.UTF-8):	Statyczne biblioteki cogl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cogl libraries.

%description static -l pl.UTF-8
Statyczne biblioteki cogl.

%package doc
Summary:	API documentation for cogl
Summary(pl.UTF-8):	Dokumentacja API cogl
Group:		Documentation

%description doc
This package contains API documentation for cogl.

%description doc -l pl.UTF-8
Ten pakiet zawiera dokumentację API cogl.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gdk-pixbuf \
	--disable-silent-rules \
	--enable-cairo \
	--enable-cogl-pango \
	--enable-glx \
	--enable-gtk-doc \
	--enable-introspection \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcogl.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcogl-pango.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcogl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcogl.so.5
%attr(755,root,root) %{_libdir}/libcogl-pango.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcogl-pango.so.0
%{_libdir}/girepository-1.0/Cogl-1.0.typelib
%{_libdir}/girepository-1.0/CoglPango-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcogl.so
%attr(755,root,root) %{_libdir}/libcogl-pango.so
%{_includedir}/cogl
%{_pkgconfigdir}/cogl-1.0.pc
%{_pkgconfigdir}/cogl-2.0-experimental.pc
%{_pkgconfigdir}/cogl-gl-1.0.pc
%{_pkgconfigdir}/cogl-pango-1.0.pc
%{_pkgconfigdir}/cogl-pango-2.0-experimental.pc
%{_datadir}/gir-1.0/Cogl-1.0.gir
%{_datadir}/gir-1.0/CoglPango-1.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcogl.a
%{_libdir}/libcogl-pango.a
%endif

%files doc
%defattr(644,root,root,755)
%{_gtkdocdir}/cogl
%{_gtkdocdir}/cogl-2.0-experimental
