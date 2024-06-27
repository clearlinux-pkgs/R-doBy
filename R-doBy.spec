#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v12
# autospec commit: a5d3013
#
Name     : R-doBy
Version  : 4.6.22
Release  : 2
URL      : https://cran.r-project.org/src/contrib/doBy_4.6.22.tar.gz
Source0  : https://cran.r-project.org/src/contrib/doBy_4.6.22.tar.gz
Summary  : Groupwise Statistics, LSmeans, Linear Estimates, Utilities
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Deriv
Requires: R-broom
Requires: R-cowplot
Requires: R-dplyr
Requires: R-ggplot2
Requires: R-microbenchmark
Requires: R-modelr
Requires: R-rlang
Requires: R-tibble
Requires: R-tidyr
BuildRequires : R-Deriv
BuildRequires : R-broom
BuildRequires : R-cowplot
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-microbenchmark
BuildRequires : R-modelr
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
## doBy
Groupwise Statistics, LSmeans, Linear Contrasts, Utilities
1. Facilities for working with grouped data: 'do' something to data stratified 'by' some variables.
2. LSmeans (least-squares means), general linear contrasts.
3. Miscellaneous utilities
4. Miscellaneous datasets

%prep
%setup -q -n doBy

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719526131

%install
export SOURCE_DATE_EPOCH=1719526131
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/doBy/DESCRIPTION
/usr/lib64/R/library/doBy/INDEX
/usr/lib64/R/library/doBy/Meta/Rd.rds
/usr/lib64/R/library/doBy/Meta/data.rds
/usr/lib64/R/library/doBy/Meta/features.rds
/usr/lib64/R/library/doBy/Meta/hsearch.rds
/usr/lib64/R/library/doBy/Meta/links.rds
/usr/lib64/R/library/doBy/Meta/nsInfo.rds
/usr/lib64/R/library/doBy/Meta/package.rds
/usr/lib64/R/library/doBy/Meta/vignette.rds
/usr/lib64/R/library/doBy/NAMESPACE
/usr/lib64/R/library/doBy/NEWS.md
/usr/lib64/R/library/doBy/R/doBy
/usr/lib64/R/library/doBy/R/doBy.rdb
/usr/lib64/R/library/doBy/R/doBy.rdx
/usr/lib64/R/library/doBy/WORDLIST
/usr/lib64/R/library/doBy/data/Rdata.rdb
/usr/lib64/R/library/doBy/data/Rdata.rds
/usr/lib64/R/library/doBy/data/Rdata.rdx
/usr/lib64/R/library/doBy/doc/doby.R
/usr/lib64/R/library/doBy/doc/doby.html
/usr/lib64/R/library/doBy/doc/doby.rmd
/usr/lib64/R/library/doBy/doc/index.html
/usr/lib64/R/library/doBy/doc/linest_lsmeans.R
/usr/lib64/R/library/doBy/doc/linest_lsmeans.pdf
/usr/lib64/R/library/doBy/doc/linest_lsmeans.rnw
/usr/lib64/R/library/doBy/doc/model_stability.R
/usr/lib64/R/library/doBy/doc/model_stability.html
/usr/lib64/R/library/doBy/doc/model_stability.rmd
/usr/lib64/R/library/doBy/doc/section_fun.R
/usr/lib64/R/library/doBy/doc/section_fun.html
/usr/lib64/R/library/doBy/doc/section_fun.rmd
/usr/lib64/R/library/doBy/help/AnIndex
/usr/lib64/R/library/doBy/help/aliases.rds
/usr/lib64/R/library/doBy/help/doBy.rdb
/usr/lib64/R/library/doBy/help/doBy.rdx
/usr/lib64/R/library/doBy/help/paths.rds
/usr/lib64/R/library/doBy/html/00Index.html
/usr/lib64/R/library/doBy/html/R.css
/usr/lib64/R/library/doBy/tests/testthat.R
/usr/lib64/R/library/doBy/tests/testthat/test-restrict.R
