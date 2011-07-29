Summary:	A library for using 3D graphics hardware to draw pretty pictures
Name:		cogl
Version:	1.7.4
Release:	1
License:	LGPL v2+
Group:		Development/Libraries
Source0:	http://www.clutter-project.org/sources/cogl/1.7/%{name}-%{version}.tar.xz
# Source0-md5:	ad6937676e0df43be5befe7dc13084cd
URL:		http://www.clutter-project.org/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel

%description
Cogl is a small open source library for using 3D graphics hardware to
draw pretty pictures. The API departs from the flat state machine
style of OpenGL and is designed to make it easy to write orthogonal
components that can render without stepping on each others toes.

As well aiming for a nice API, we think having a single library as
opposed to an API specification like OpenGL has a few advantages too;
like being able to paper over the inconsistencies/bugs of different
OpenGL implementations in a centralized place, not to mention the
myriad of OpenGL extensions. It also means we are in a better position
to provide utility APIs that help software developers since they only
need to be implemented once and there is no risk of inconsistency
between implementations.

Having other backends, besides OpenGL, such as drm, Gallium or D3D are
options we are interested in for the future.

%package devel
Summary:	%{name} development environment
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLX-devel
Requires:	cairo-devel
Requires:	glib2-devel
Requires:	gobject-introspection-devel
Requires:	pango-devel
Requires:	pkgconfig

%description devel
Header files and libraries for building and developing apps with
%{name}.

%package       doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description   doc
This package contains documentation for %{name}.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS -fPIC"

%configure \
	--enable-cairo=yes \
	--enable-gdk-pixbuf=no \
	--enable-cogl-pango=yes \
	--enable-glx=yes \
	--enable-gtk-doc \
	--enable-introspection=yes \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcogl.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcogl-pango.la

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING NEWS README ChangeLog
%attr(755,root,root) %{_libdir}/libcogl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcogl.so.2
%attr(755,root,root) %{_libdir}/libcogl-pango.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcogl-pango.so.0
%{_libdir}/girepository-1.0/Cogl-1.0.typelib
%{_libdir}/girepository-1.0/CoglPango-1.0.typelib

%files devel
%defattr(644,root,root,755)
%{_includedir}/cogl
%{_libdir}/libcogl.so
%{_libdir}/libcogl-pango.so
%{_pkgconfigdir}/cogl-1.0.pc
%{_pkgconfigdir}/cogl-2.0-experimental.pc
%{_pkgconfigdir}/cogl-gl-1.0.pc
%{_pkgconfigdir}/cogl-pango-1.0.pc
%{_pkgconfigdir}/cogl-pango-2.0-experimental.pc
%{_datadir}/gir-1.0/Cogl-1.0.gir
%{_datadir}/gir-1.0/CoglPango-1.0.gir

%files doc
%defattr(644,root,root,755)
%{_gtkdocdir}/cogl
%{_gtkdocdir}/cogl-2.0-experimental
