#! /usr/bin/perl

# Read the CPU temperture, determine scale, and write to STDOUT

use strict;

open TEMP, "</sys/class/thermal/thermal_zone0/temp";
my $ctemp = <TEMP>;
close TEMP;
chomp $ctemp;

if ($ctemp > 1000) {
  $ctemp /= 1000;
}

my $ftemp = $ctemp * 9 / 5 + 32;

my @ts = localtime();
my $timestamp = sprintf("%04d-%02d-%02d %02d:%02d", 
	$ts[5]+1900, $ts[4]+1, $ts[3],
	$ts[2], $ts[1]);
printf "\"%s\", %5.1f\n", $timestamp, $ftemp;
