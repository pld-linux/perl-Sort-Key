#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	Key
Summary:	Sort::Key - interface to sort arrays by one or manipulate calculated keys
Summary(pl):	Sort::Key - interfejs do szybkiego sortowania tablic wed�ug zmiennych kluczy
Name:		perl-Sort-Key
Version:	1.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5fb7a2c8d477ef3eb0f56652d39ec3c2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort arrays by one or multiple calculated keys.

%description -l pl
Sort arrays by one or multiple calculated keys.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorarch}/Sort/*
%{perl_vendorarch}/Sort/Key/*
%dir %{perl_vendorarch}/auto/Sort/Key/*
%{perl_vendorarch}/auto/Sort/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Sort/*/*.so
%{_mandir}/man3/*
