##########################################
# load csv serp file and aggregate the data
# to create a new csv file where each line is
# a website and each column is a query.
#
# only best postion is kept for each query
#
# perl aggregate.pl> aggregated_signals_20_en.csv
#
##########################################
use strict;

# read the input csv serp file, please uncomment the one you want to process
#open(my $fh, "<", "signals_20_ch_fr.csv")
open(my $fh, "<", "signals_20_en.csv")
#open(my $fh, "<", "signals_covid_20_en.csv")
#open(my $fh, "<", "signals_covid_20_ch_fr.csv")
    or die "Can't open < input.txt: $!";

my $line = <$fh>;
my %domains; # hash to keep all the domains (aka websites)
my %queries; # hash to keep all the queries
my %dom_que; # hash to keep combination of domain and query
my $past_query = ''; # keep previous query (to know when to change in the serp)
my $count = 0;
# process csv line by line
while (my $line = <$fh>) {
  my @tab     = split /\t/,$line;

  my $rank    = $tab[4]; #rank of the website for this query in the serp
  my $domain  = $tab[9]; #domain of the website
  my $query   = $tab[3]; #query
  my $type    = $tab[5]; #type of serp results

  # count = 0 only if query change in the SERP
  if ((!$past_query) || ($past_query eq $query)) {
  }
  else {
    $count = 0;
  }
  # keep only serp of type results
  if ($type eq 'results') {
    $count++;
    $domains{$domain} = 1; # add in the hash this domain value
    $queries{$query}  = 1; # add in the hash this query value
    # if first combination of domain and query
    if (not $dom_que{$domain.'_'.$query}) {
      $dom_que{$domain.'_'.$query} = $count; # we keep the count which is the relevant position
    }
    $past_query = $query; # remember previous query for next line
  }
}


# prepare the first line of the csv with query name
# alphabetic ordered
print "domain\t";
my $nb = 0;
foreach my $q (sort(keys %queries)) {
  print "$q\t";
  $nb++;
}
print "total\t";
print "missing\n";

# create de new csv line
foreach my $d (sort(keys %domains)) { # first by domain (website)
    print "$d\t";
    my $total = 0;
    my $missing = 0;
    # loop on all queries by alphebetic order
    foreach my $q (sort(keys %queries)) {
      my $rank = 30; # arbitrary default max rank
      if ($dom_que{$d.'_'.$q}) {
        $rank = $dom_que{$d.'_'.$q};
      }
      else {
        $missing++; # count missing site for this query
      }
      $total += $rank;
      print "$rank\t"; # the rank is the one counted
    }
  my $total_rank =  $total/$nb; # computed average rank
  print $total_rank."\t";
  print "$missing\n";
}
