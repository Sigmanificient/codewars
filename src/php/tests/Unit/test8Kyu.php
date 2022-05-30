<?php

declare(strict_types=1);

namespace Tests\Unit;

use PHPUnit\Framework\TestCase;

require_once dirname(__DIR__, 2) . '/katas/8kyu/return_negative.php';

class Test8Kyu extends TestCase
{
    /** @covers ::makeNegative */
    /** @test */
    public function TestMakeNegative()
    {
        $this->assertEquals(0, makeNegative(0));
        $this->assertEquals(-1, makeNegative(1));
        $this->assertEquals(-1, makeNegative(-1));
        $this->assertEquals(-42, makeNegative(42));
        $this->assertEquals(-69, makeNegative(-69));
    }
}