Name:           perl-Math-Int64
Version:        0.54
Release:        1%{?dist}
Summary:        Manipulate 64 bits integers in Perl
License:        GPL

Group:          Development/Libraries
URL:            http://metacpan.org/release/Math-Int64
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/Math-Int64-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module adds support for 64 bit integers, signed and unsigned, to Perl.

%prep
%setup -q -n Math-Int64-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%files
%defattr(-,root,root,-)
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*.3*

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 0.54
- Package creation for production usage on amzn 2017.03
