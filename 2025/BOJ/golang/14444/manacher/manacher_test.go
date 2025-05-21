package manacher

import "testing"

func TestManacher(t *testing.T) {
	tests := []struct {
		input    string
		expected int
	}{
		{"abba", 4},
		{"racecar", 7},
		{"banana", 5},
		{"abc", 1},
		{"a", 1},
		{"", 0},
		{"abacdfgdcaba", 3},
	}

	for _, tc := range tests {
		got := Manacher(tc.input)
		if got != tc.expected {
			t.Errorf("manacher(%q) = %d; want %d", tc.input, got, tc.expected)
		}
	}
}
