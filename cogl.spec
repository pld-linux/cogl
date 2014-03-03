#
# Conditional build
%bcond_without	static_libs	# static libraries
%bcond_without	gdkpixbuf	# gdk-pixbuf for image loading [instead of stb_image]
%bcond_without	gles1		# OpenGL-ES 1.1 support
%bcond_without	gles2		# OpenGL-ES 2.0 support
%bcond_without	kms		# KMS EGL support
%bcond_without	gstreamer	# GStreamer support
%bcond_without	wayland		# Wayland EGL support
#
Summary:	A library for using 3D graphics hardware to draw pretty pictures
Summary(pl.UTF-8):	Biblioteka do rysowania ładnych obrazków przy użyciu sprzętowej grafiki 3D
Name:		cogl
Version:	1.17.4
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cogl/1.17/%{name}-%{version}.tar.xz
# Source0-md5:	6f8f3a6652de35eafc37ebbf95d09e17
Patch0:		%{name}-link.patch
URL:		http://www.clutter-project.org/
%{?with_wayland:BuildRequires:	EGL-devel}
%{?with_kms:BuildRequires:	Mesa-libgbm-devel}
%{?with_wayland:BuildRequires:	Mesa-libwayland-egl-devel >= 1.0.0}
%{?with_gles1:BuildRequires:	OpenGLESv1-devel >= 1.1}
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.10
%{?with_gdkpixbuf:BuildRequires:	gdk-pixbuf2-devel >= 2.0}
BuildRequires:	gettext-devel >= 0.18.1
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
%{?with_gstreamer:BuildRequires:	gstreamer-devel >= 1.0}
%{?with_gstreamer:BuildRequires:	gstreamer-plugins-base-devel >= 1.0}
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	libdrm-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pango-devel >= 1:1.20
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
# wayland-client >= 1.0.0, wayland-server >= 1.1.90
%{?with_wayland:BuildRequires:	wayland-devel >= 1.2.0}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.4
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel >= 3
BuildRequires:	xorg-lib-libXrandr-devel >= 1.2
BuildRequires:	xz
Requires:	cairo >= 1.10
Requires:	glib2 >= 1:2.32.0
Requires:	pango >= 1:1.20
%{?with_wayland:Requires:	wayland >= 1.2.0}
Requires:	xorg-lib-libXcomposite >= 0.4
Requires:	xorg-lib-libXfixes >= 3
Requires:	xorg-lib-libXrandr >= 1.2
Suggests:	OpenGL
%{?with_gles1:Provides:	cogl(gles1) = %{version}-%{release}}
%{?with_gles2:Provides:	cogl(gles2) = %{version}-%{release}}
%{?with_kms:Provides:	cogl(kms) = %{version}-%{release}}
%{?with_wayland:Provides:	cogl(wayland) = %{version}-%{release}}
Conflicts:	clutter < 1.8.0
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
%{?with_wayland:Requires:	EGL-devel}
%{?with_kms:Requires:	Mesa-libgbm-devel}
%{?with_wayland:Requires:	Mesa-libwayland-egl-devel >= 1.0.0}
Requires:	cairo-devel >= 1.10
%{?with_gdkpixbuf:Requires:	gdk-pixbuf2-devel >= 2.0}
Requires:	glib2-devel >= 1:2.32.0
Requires:	gobject-introspection-devel >= 0.9.5
Requires:	libdrm-devel
Requires:	pango-devel >= 1:1.20
%{?with_wayland:Requires:	wayland-devel >= 1.2.0}
Requires:	xorg-lib-libXcomposite-devel >= 0.4
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel >= 3
Requires:	xorg-lib-libXrandr-devel >= 1.2
%{?with_gles1:Provides:	cogl-devel(gles1) = %{version}-%{release}}
%{?with_gles2:Provides:	cogl-devel(gles2) = %{version}-%{release}}
%{?with_kms:Provides:	cogl-devel(kms) = %{version}-%{release}}
%{?with_wayland:Provides:	cogl-devel(wayland) = %{version}-%{release}}
Conflicts:	clutter-devel < 1.8.0

%description devel
Header files for building and developing applications with cogl.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji z użyciem biblioteki cogl.

%package static
Summary:	Static cogl libraries
Summary(pl.UTF-8):	Statyczne biblioteki cogl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%{?with_gles1:Provides:	cogl-static(gles1) = %{version}-%{release}}
%{?with_gles2:Provides:	cogl-static(gles2) = %{version}-%{release}}
%{?with_kms:Provides:	cogl-static(kms) = %{version}-%{release}}
%{?with_wayland:Provides:	cogl-static(wayland) = %{version}-%{release}}
Conflicts:	clutter-static < 1.8.0

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

%package gles2
Summary:	Cogl frontend library for OpenGL-ES 2.0
Summary(pl.UTF-8):	Biblioteka frontendowa Cogl dla OpenGL-ES 2.0
Group:		Libraries
Requires:	%{name}(gles2) = %{version}-%{release}

%description gles2
Cogl frontend library for OpenGL-ES 2.0.

%description gles2 -l pl.UTF-8
Biblioteka frontendowa Cogl dla OpenGL-ES 2.0.

%package gles2-devel
Summary:	Header files for cogl-gles2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cogl-gles2
Group:		Development/Libraries
Requires:	%{name}-devel(gles2) = %{version}-%{release}
Requires:	%{name}-gles2 = %{version}-%{release}

%description gles2-devel
Header files for cogl-gles2 library.

%description gles2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cogl-gles2.

%package gles2-static
Summary:	Static cogl-gles2 library
Summary(pl.UTF-8):	Statyczna biblioteka cogl-gles2
Group:		Development/Libraries
Requires:	%{name}-gles2-devel = %{version}-%{release}

%description gles2-static
Static cogl-gles2 library.

%description gles2-static -l pl.UTF-8
Statyczna biblioteka cogl-gles2.

%package gst
Summary:	GStreamer integration library for Cogl
Summary(pl.UTF-8):	Biblioteka integrująca GStreamera z Cogl
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gst
GStreamer integration library for Cogl.

%description gst -l pl.UTF-8
Biblioteka integrująca GStreamera z Cogl.

%package gst-devel
Summary:	Header files for cogl-gst library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cogl-gst
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gst = %{version}-%{release}
Requires:	gstreamer-devel >= 1.0
Requires:	gstreamer-plugins-base-devel >= 1.0

%description gst-devel
Header files for cogl-gst library.

%description gst-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cogl-gst.

%package gst-static
Summary:	Static cogl-gst library
Summary(pl.UTF-8):	Statyczna biblioteka cogl-gst
Group:		Development/Libraries
Requires:	%{name}-gst-devel = %{version}-%{release}

%description gst-static
Static cogl-gst library.

%description gst-static -l pl.UTF-8
Statyczna biblioteka cogl-gst.

%package gst-apidocs
Summary:	API documentation for cogl-gst library
Summary(pl.UTF-8):	Dokumentacja API biblioteki cogl-gst
Group:		Documentation

%description gst-apidocs
API documentation for cogl-gst library.

%description gst-apidocs -l pl.UTF-8
Dokumentacja API biblioteki cogl-gst.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_gdkpixbuf:--disable-gdk-pixbuf} \
	--disable-silent-rules \
	--enable-cairo \
	%{?with_gstreamer:--enable-cogl-gst} \
	--enable-cogl-pango \
	%{?with_gles1:--enable-gles1 --with-gles1-libname=libGLESv1_CM.so.1} \
	%{?with_gles2:--enable-gles2 --with-gles2-libname=libGLESv2.so.2} \
	--enable-glx \
	--enable-gtk-doc \
	--enable-introspection \
	--enable-kms-egl-platform \
	%{?with_static_libs:--enable-static} \
	%{?with_wayland:--enable-wayland-egl-platform} \
	%{?with_wayland:--enable-wayland-egl-server} \
	--enable-xlib-egl-platform \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with gstreamer}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstcogl.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstcogl.a
%endif
%endif
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcogl*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gles2 -p /sbin/ldconfig
%postun	gles2 -p /sbin/ldconfig

%post	gst -p /sbin/ldconfig
%postun	gst -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcogl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcogl.so.20
%attr(755,root,root) %{_libdir}/libcogl-pango.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcogl-pango.so.20
%attr(755,root,root) %{_libdir}/libcogl-path.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcogl-path.so.20
%{_libdir}/girepository-1.0/Cogl-1.0.typelib
%{_libdir}/girepository-1.0/CoglPango-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcogl.so
%attr(755,root,root) %{_libdir}/libcogl-pango.so
%attr(755,root,root) %{_libdir}/libcogl-path.so
%dir %{_includedir}/cogl
%{_includedir}/cogl/cogl
%{_includedir}/cogl/cogl-pango
%{_includedir}/cogl/cogl-path
%{_pkgconfigdir}/cogl-1.0.pc
%{_pkgconfigdir}/cogl-2.0-experimental.pc
%{_pkgconfigdir}/cogl-gl-1.0.pc
%{_pkgconfigdir}/cogl-pango-1.0.pc
%{_pkgconfigdir}/cogl-pango-2.0-experimental.pc
%{_pkgconfigdir}/cogl-path-1.0.pc
%{_pkgconfigdir}/cogl-path-2.0-experimental.pc
%{_datadir}/gir-1.0/Cogl-1.0.gir
%{_datadir}/gir-1.0/CoglPango-1.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcogl.a
%{_libdir}/libcogl-pango.a
%{_libdir}/libcogl-path.a
%endif

%files doc
%defattr(644,root,root,755)
%{_gtkdocdir}/cogl
%{_gtkdocdir}/cogl-2.0-experimental

%if %{with gles2}
%files gles2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcogl-gles2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcogl-gles2.so.20

%files gles2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcogl-gles2.so
%{_includedir}/cogl/cogl-gles2
%{_pkgconfigdir}/cogl-gles2-1.0.pc
%{_pkgconfigdir}/cogl-gles2-2.0-experimental.pc

%if %{with static_libs}
%files gles2-static
%defattr(644,root,root,755)
%{_libdir}/libcogl-gles2.a
%endif
%endif

%if %{with gstreamer}
%files gst
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcogl-gst.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcogl-gst.so.20
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstcogl.so

%files gst-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcogl-gst.so
%{_includedir}/cogl/cogl-gst
%{_pkgconfigdir}/cogl-gst-1.0.pc
%{_pkgconfigdir}/cogl-gst-2.0-experimental.pc

%if %{with static_libs}
%files gst-static
%defattr(644,root,root,755)
%{_libdir}/libcogl-gst.a
%endif

%files gst-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cogl-gst
%endif
