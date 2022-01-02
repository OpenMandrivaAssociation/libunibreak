%define         libversion 5
%define         altver  5_0
Name:           libunibreak
Version:        5.0
Release:        1
Summary:        Unicode line-breaking library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/adah1972/libunibreak
Source0:        https://github.com/adah1972/libunibreak/releases/download/libunibreak_%{altver}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
Libunibreak is the successor of liblinebreak, an implementation of the line
breaking algorithm as described in Unicode 6.0.0 Standard Annex 14, Revision
26, available at http://www.unicode.org/reports/tr14/tr14-26.html

It is designed to be used in a generic text renderer. FBReader is one
real-world example, and you may also check some simple sample code, like
showbreak and breaktext.

%package devel
Summary:        Development files for libunibreak
Group:          Development/Libraries/C and C++
Requires:       %{name}%{libversion} = %{version}
Requires:       pkgconfig

Provides:       liblinebreak-devel = 2.1

%description devel
The libunibreak-devel package contains libraries and header files for
developing applications that use libunibreak.

%package -n libunibreak%{libversion}
Summary:        Unicode line-breaking library
Group:          Development/Libraries/C and C++

%description -n libunibreak%{libversion}
Libunibreak is an implementation of the line breaking and word breaking
algorithm as described in Unicode Standard Annex 14 and Unicode Standard
Annex 29.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure \
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.*a' -print -delete

%files -n libunibreak%{libversion}
%license LICENCE
%{_libdir}/*.so.%{libversion}{,.*}

%files devel
%license LICENCE
%doc AUTHORS NEWS README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libunibreak.pc
