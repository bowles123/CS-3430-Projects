# Brian Bowles, Assignment 9: Smallest Divisible, March 24, 2015.

use warnings;
use strict;

sub smallest
{
	my $num = 20;
	
	while(1)
	{
		if (($num%7) == 0 && ($num%11) == 0 && ($num%12) == 0   
		&& ($num%13) == 0 && ($num%14) == 0 && ($num%15) == 0 
		&& ($num%16) == 0 && ($num%17) == 0 && ($num%18)== 0
		&& ($num%19) == 0 && ($num%20) == 0)
		{
			print 'The lowest divisible number from 1-20 is: '.$num.'.';
			last;
		}
		$num = $num + 20;
	}
	die;
}

smallest();