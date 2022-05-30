<?php

declare(strict_types=1);

namespace Tests\Unit;

define('ROOT', dirname(__DIR__, 2));
require ROOT . '/katas/8kyu/return_negative.php';

class Test8Kyu extends \PHPUnit\Framework\TestCase
{
    /** @test */
    public function makeNegative()
    {
        $this->assertEquals(0, makeNegative(0));
        $this->assertEquals(-1, makeNegative(1));
        $this->assertEquals(-1, makeNegative(-1));
        $this->assertEquals(-42, makeNegative(42));
        $this->assertEquals(-69, makeNegative(-69));
    }
}