#!/usr/bin/perl
# CM Monday 13 December 2010 

#takes a file of peptides (peptide sequence on one line, no line break in sequence)
$pipeline_dir="/usr/lib/cgi-bin/afpp";

if(@ARGV < 2){
	print "Usage: ./Afpp.pl input_file output_file\n";
	exit(0);
}

$fasta = shift @ARGV;
$out_file = shift @ARGV;

open(ferr,">$fasta.err");

print ferr  "fasta $fasta\n";

print ferr "$fasta.err\n";

open(fin,"<$fasta");
@fasta = <fin>;
close fin;  

while(@fasta){
	$sequence = shift @fasta;
	$sequence =~ s/\s+$//; 

	$length =length($sequence);
		
	open (ft, ">$fasta.dataset");
	print ft "1\npeptide\n$length\n$sequence\n1\n";
	close ft;

   	print ferr  "1\npeptide\n$length\n$sequence\n1\n";

	if($sequence ne ""){

		system("$pipeline_dir/Afpp $pipeline_dir/Models.txt $fasta.dataset ./ ");


		print ferr "$fasta.dataset.predictions\n";

		open(fin,"<$fasta.dataset.predictions");
		@pred = <fin>;
		close fin;  

		shift @pred;
		shift @pred;
		shift @pred;
		shift @pred;
		shift @pred;
		$prediction = shift @pred;
		chop $prediction;
		@foo = split(/ /, $prediction);
		$prediction = $foo[1];

		print ferr "prediction $prediction\n";

		push(@all,  "$prediction\t$sequence");
	}
	

}

@all = reverse sort(@all);

open(f,">$out_file");

for($i=0;$i<@all;$i++){
	print f "$all[$i]\n";
}

close f;
close ferr;

exit;
