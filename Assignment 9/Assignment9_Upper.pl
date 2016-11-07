# Brian Bowles, Assignment 9: Upper Bound, March 24, 2015.

use warnings;
use strict;

sub upper
{
	print 'Please enter the upperbound for the interval: ';
	my $upperbound = <STDIN>;
	my $sum = 0;
	my $i = 1;

	for (;$i < $upperbound; $i++)
	{
		if(($i % 3) == 0 || ($i % 5) == 0)
		{
			$sum += $i;
		}
	}
	print 'The sum of the multiples of 3 or 5 in [1, '.$upperbound.') is: '.$sum;
}

upper();
