# PostgreSQL POSIX Regular Expressions Guide

*Source: [PostgreSQL Documentation - Pattern Matching](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP)*

*Last updated: August 14, 2025*

---

## Table of Contents

1. [Introduction](#introduction)
2. [Regular Expression Operators](#regular-expression-operators)
3. [Essential Regular Expression Functions](#essential-regular-expression-functions)
4. [Regular Expression Flags](#regular-expression-flags)
5. [Common Pattern Examples](#common-pattern-examples)
6. [Character Classes and Shortcuts](#character-classes-and-shortcuts)
7. [Advanced Features](#advanced-features)
8. [Performance Considerations](#performance-considerations)
9. [Security Warnings](#security-warnings)
10. [Detailed Function Reference](#detailed-function-reference)
11. [Pattern Syntax](#pattern-syntax)
12. [Examples and Use Cases](#examples-and-use-cases)

---

## Introduction

PostgreSQL provides comprehensive POSIX regular expression support that goes far beyond basic pattern matching. This guide covers the full range of PostgreSQL's regex capabilities, from simple case-insensitive searches to complex pattern extraction and text manipulation.

PostgreSQL implements Advanced Regular Expressions (AREs) which are nearly a superset of Extended Regular Expressions (EREs) and Basic Regular Expressions (BREs).

---

## Regular Expression Operators

### Basic Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `~` | String matches regex (case sensitive) | `'thomas' ~ 't.*ma'` | `true` |
| `~*` | String matches regex (case insensitive) | `'thomas' ~* 'T.*ma'` | `true` |
| `!~` | String does NOT match regex (case sensitive) | `'thomas' !~ 't.*max'` | `true` |
| `!~*` | String does NOT match regex (case insensitive) | `'thomas' !~* 'T.*ma'` | `false` |

### Examples

```sql
-- Case-sensitive matching
SELECT 'Hello World' ~ 'hello';          -- false
SELECT 'Hello World' ~ 'Hello';          -- true

-- Case-insensitive matching  
SELECT 'Hello World' ~* 'hello';         -- true
SELECT 'Hello World' ~* 'WORLD';         -- true

-- Negative matching
SELECT 'Hello World' !~ 'goodbye';       -- true
SELECT 'Hello World' !~* 'GOODBYE';      -- true
```

---

## Essential Regular Expression Functions

### 1. `regexp_like()` - Boolean Match Check

**Syntax:** `regexp_like(string, pattern [, flags])`

**Purpose:** Returns boolean true/false if pattern matches

```sql
-- Basic usage
SELECT regexp_like('Hello World', 'world');        -- false
SELECT regexp_like('Hello World', 'world', 'i');   -- true (case-insensitive)

-- Email validation
SELECT regexp_like('user@domain.com', '^[^@]+@[^@]+\.[^@]+$');  -- true

-- Phone number check
SELECT regexp_like('(555) 123-4567', '^\(\d{3}\) \d{3}-\d{4}$'); -- true
```

### 2. `regexp_match()` - Extract First Match

**Syntax:** `regexp_match(string, pattern [, flags])`

**Purpose:** Returns array of captured groups from first match

```sql
-- Simple extraction
SELECT regexp_match('foobarbequebaz', 'bar.*que');
-- Result: {barbeque}

-- Capturing groups
SELECT regexp_match('foobarbequebaz', '(bar)(beque)');
-- Result: {bar,beque}

-- Extract date components
SELECT regexp_match('2024-12-25', '(\d{4})-(\d{2})-(\d{2})');
-- Result: {2024,12,25}

-- Extract from mixed text
SELECT regexp_match('Price: $123.45', '\$(\d+)\.(\d+)');
-- Result: {123,45}
```

### 3. `regexp_matches()` - Extract All Matches

**Syntax:** `regexp_matches(string, pattern [, flags])`

**Purpose:** Returns set of arrays for all matches (use 'g' flag)

```sql
-- Find all matches
SELECT regexp_matches('foobarbequebazilbarfbonk', '(b[^b]+)(b[^b]+)', 'g');
-- Result: 
-- {bar,beque}
-- {bazil,barf}

-- Extract all words
SELECT regexp_matches('Hello World Test', '\w+', 'g');
-- Result:
-- {Hello}
-- {World}
-- {Test}

-- Find all email addresses in text
SELECT regexp_matches(
    'Contact john@example.com or mary@test.org', 
    '([^@\s]+@[^@\s]+\.[^@\s]+)', 
    'g'
);
```

### 4. `regexp_replace()` - Search and Replace

**Syntax:** `regexp_replace(source, pattern, replacement [, start [, N]] [, flags])`

**Purpose:** Replace pattern matches with replacement text

```sql
-- Basic replacement
SELECT regexp_replace('foobarbaz', 'b..', 'X');
-- Result: fooXbaz

-- Global replacement
SELECT regexp_replace('foobarbaz', 'b..', 'X', 'g');
-- Result: fooXX

-- Using capture groups (\1, \2, etc.)
SELECT regexp_replace('foobarbaz', 'b(..)', 'X\1Y', 'g');
-- Result: fooXarYXazY

-- Replace specific occurrence
SELECT regexp_replace('test test test', 'test', 'REPLACED', 2);
-- Result: test REPLACED test

-- Phone number formatting
SELECT regexp_replace('5551234567', '(\d{3})(\d{3})(\d{4})', '(\1) \2-\3');
-- Result: (555) 123-4567

-- Remove HTML tags
SELECT regexp_replace('<p>Hello <b>World</b></p>', '<[^>]*>', '', 'g');
-- Result: Hello World
```

### 5. `regexp_count()` - Count Matches

**Syntax:** `regexp_count(string, pattern [, start [, flags]])`

**Purpose:** Count number of pattern matches

```sql
-- Count occurrences
SELECT regexp_count('ABCABCAXYaxy', 'A.');          -- 3
SELECT regexp_count('ABCABCAXYaxy', 'A.', 1, 'i');  -- 4 (case-insensitive)

-- Count words
SELECT regexp_count('Hello World Test', '\w+');     -- 3

-- Count digits
SELECT regexp_count('abc123def456ghi', '\d');       -- 6
```

### 6. `regexp_split_to_table()` - Split String

**Syntax:** `regexp_split_to_table(string, pattern [, flags])`

**Purpose:** Split string into rows using pattern as delimiter

```sql
-- Split by whitespace
SELECT foo FROM regexp_split_to_table('the quick brown fox jumps', '\s+') AS foo;
-- Returns: the, quick, brown, fox, jumps (each as separate row)

-- Split CSV data
SELECT value FROM regexp_split_to_table('apple,banana,cherry', ',') AS value;

-- Split by multiple delimiters
SELECT part FROM regexp_split_to_table('one;two:three,four', '[;:,]') AS part;
```

### 7. `regexp_split_to_array()` - Split to Array

**Syntax:** `regexp_split_to_array(string, pattern [, flags])`

**Purpose:** Split string into array using pattern as delimiter

```sql
-- Split into array
SELECT regexp_split_to_array('the quick brown fox', '\s+');
-- Result: {the,quick,brown,fox}

-- Split path
SELECT regexp_split_to_array('/usr/local/bin', '/');
-- Result: {"",usr,local,bin}
```

---

## Regular Expression Flags

| Flag | Description | Example |
|------|-------------|---------|
| `i` | Case-insensitive matching | `regexp_like('Hello', 'hello', 'i')` |
| `g` | Global matching (find all matches) | `regexp_replace('test test', 'test', 'X', 'g')` |
| `m` | Multi-line mode (^ and $ match line boundaries) | Pattern treats each line separately |
| `n` | Newline-sensitive matching | `.` doesn't match newline |
| `s` | Dot matches newline | `.` matches any character including newline |
| `x` | Extended syntax (ignore whitespace and comments) | Allows formatted regex patterns |

### Flag Examples

```sql
-- Case-insensitive
SELECT regexp_replace('Hello WORLD', 'hello', 'Hi', 'i');  -- Hi WORLD

-- Global replacement
SELECT regexp_replace('test test test', 'test', 'X', 'g'); -- X X X

-- Multi-line mode
SELECT regexp_matches(E'line1\nline2\nline3', '^line', 'gm');
-- Matches 'line' at start of each line

-- Extended syntax with comments
SELECT regexp_like('test123', '(?x)
    test    # Match literal "test"
    \d+     # Match one or more digits
');
```

---

## Common Pattern Examples

### Email Validation

```sql
-- Basic email pattern
SELECT regexp_like(
    'user@example.com', 
    '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
);

-- More comprehensive email validation
SELECT regexp_like(
    'user.name+tag@example-domain.co.uk',
    '^[a-zA-Z0-9.!#$%&''*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
);
```

### Phone Number Extraction

```sql
-- US phone number with parentheses
SELECT regexp_match(
    'Call me at (555) 123-4567', 
    '\((\d{3})\)\s*(\d{3})-(\d{4})'
);
-- Result: {555,123,4567}

-- Multiple phone formats
SELECT regexp_match(
    'Phone: 555-123-4567 or 555.123.4567',
    '(\d{3})[-.](\d{3})[-.](\d{4})'
);

-- International format
SELECT regexp_match(
    '+1-555-123-4567',
    '^\+(\d{1,3})-(\d{3})-(\d{3})-(\d{4})$'
);
```

### URL Parsing

```sql
-- Basic URL components
SELECT regexp_match(
    'https://www.example.com/path?param=value',
    '^(https?)://([^/]+)(/[^?]*)?(\?.*)?$'
);
-- Result: {https,www.example.com,/path,?param=value}

-- Extract domain only
SELECT regexp_match(
    'https://subdomain.example.com:8080/path',
    '://([^:/]+)'
);
-- Result: {subdomain.example.com}
```

### Date and Time Patterns

```sql
-- ISO date format
SELECT regexp_match('2024-12-25', '(\d{4})-(\d{2})-(\d{2})');
-- Result: {2024,12,25}

-- US date format
SELECT regexp_match('12/25/2024', '(\d{1,2})/(\d{1,2})/(\d{4})');
-- Result: {12,25,2024}

-- Time format
SELECT regexp_match('14:30:45', '(\d{2}):(\d{2}):(\d{2})');
-- Result: {14,30,45}
```

---

## Character Classes and Shortcuts

### POSIX Character Classes

| Pattern | Description | Equivalent |
|---------|-------------|------------|
| `[:alnum:]` | Alphanumeric characters | `[A-Za-z0-9]` |
| `[:alpha:]` | Alphabetic characters | `[A-Za-z]` |
| `[:digit:]` | Numeric digits | `[0-9]` |
| `[:lower:]` | Lowercase letters | `[a-z]` |
| `[:upper:]` | Uppercase letters | `[A-Z]` |
| `[:space:]` | Whitespace characters | `[ \t\n\r\f]` |
| `[:punct:]` | Punctuation characters | Various punctuation |
| `[:word:]` | Word characters | `[A-Za-z0-9_]` |

### Character Shortcuts

| Pattern | Description | Equivalent |
|---------|-------------|------------|
| `\d` | Any digit | `[[:digit:]]` or `[0-9]` |
| `\D` | Any non-digit | `[^[:digit:]]` |
| `\w` | Word character | `[[:word:]]` or `[A-Za-z0-9_]` |
| `\W` | Non-word character | `[^[:word:]]` |
| `\s` | Whitespace | `[[:space:]]` |
| `\S` | Non-whitespace | `[^[:space:]]` |

### Examples

```sql
-- Using character classes
SELECT regexp_like('Hello123', '^[[:alpha:]]+[[:digit:]]+$');  -- true

-- Using shortcuts
SELECT regexp_replace('abc123def', '\d+', 'XXX');              -- abcXXXdef

-- Custom character class
SELECT regexp_like('test@example.com', '^[[:alnum:]._%+-]+@[[:alnum:].-]+$');
```

---

## Advanced Features

### Lookahead and Lookbehind Assertions

```sql
-- Positive lookahead (?=...)
-- Match word followed by digits
SELECT regexp_match('password123', '\w+(?=\d+)');  
-- Result: {password}

-- Negative lookahead (?!...)
-- Match word NOT followed by digits
SELECT regexp_match('password', '\w+(?!\d+)');     
-- Result: {password}

-- Positive lookbehind (?<=...)
-- Match word preceded by digits
SELECT regexp_match('123password', '(?<=\d+)\w+'); 
-- Result: {password}

-- Negative lookbehind (?<!...)
-- Match word NOT preceded by digits
SELECT regexp_match('password', '(?<!\d+)\w+');    
-- Result: {password}
```

### Non-capturing Groups

```sql
-- Use (?:...) for grouping without capturing
SELECT regexp_match('2024-12-25', '(\d{4})-(?:\d{2})-(\d{2})');
-- Result: {2024,25} (month not captured)

-- Useful for alternation without capturing
SELECT regexp_match('Mr. Smith', '(?:Mr\.|Mrs\.|Dr\.)\s+(\w+)');
-- Result: {Smith}
```

### Quantifiers

| Quantifier | Description | Example |
|------------|-------------|---------|
| `*` | Zero or more | `a*` matches "", "a", "aa", "aaa" |
| `+` | One or more | `a+` matches "a", "aa", "aaa" |
| `?` | Zero or one | `a?` matches "", "a" |
| `{n}` | Exactly n | `a{3}` matches "aaa" |
| `{n,}` | n or more | `a{3,}` matches "aaa", "aaaa", etc. |
| `{n,m}` | Between n and m | `a{2,4}` matches "aa", "aaa", "aaaa" |

### Greedy vs Non-greedy

```sql
-- Greedy quantifier (default)
SELECT regexp_match('aaaaaa', 'a{2,4}');    -- {aaaa}

-- Non-greedy quantifier (add ?)
SELECT regexp_match('aaaaaa', 'a{2,4}?');   -- {aa}

-- Practical example with HTML
SELECT regexp_replace('<b>bold</b> and <i>italic</i>', '<.*>', 'X');     -- X (greedy)
SELECT regexp_replace('<b>bold</b> and <i>italic</i>', '<.*?>', 'X', 'g'); -- X and X (non-greedy)
```

---

## Performance Considerations

### Index Usage

```sql
-- Regular expressions typically don't use indexes
EXPLAIN SELECT * FROM users WHERE email ~ '^admin';

-- Create functional index for better performance
CREATE INDEX idx_users_email_lower ON users (LOWER(email));

-- Use with ILIKE for indexed searches
SELECT * FROM users WHERE LOWER(email) LIKE 'admin%';
```

### Best Practices

1. **Simple patterns first**: Use `LIKE` or `ILIKE` when possible
2. **Anchor patterns**: Use `^` and `$` to avoid unnecessary backtracking
3. **Avoid complex alternation**: `(a|b|c|d|e)` can be slow
4. **Use character classes**: `[abcde]` is faster than `(a|b|c|d|e)`
5. **Limit backtracking**: Avoid nested quantifiers like `(a+)+`

### Performance Examples

```sql
-- Slow: Complex alternation
SELECT * FROM products WHERE name ~ '(red|blue|green|yellow|orange)';

-- Faster: Character class approach
SELECT * FROM products WHERE name ~ '(red|blue|green|yellow|orange)' 
    AND name ~ '^[rbgyo]';

-- Fastest: Use ILIKE when possible
SELECT * FROM products WHERE name ILIKE '%red%' 
    OR name ILIKE '%blue%' 
    OR name ILIKE '%green%';
```

---

## Security Warnings

### ReDoS (Regular Expression Denial of Service)

```sql
-- Dangerous pattern - can cause exponential backtracking
-- DON'T USE: (a+)+b
-- DON'T USE: (a|a)*b
-- DON'T USE: (a*)*b

-- Safe alternative
SELECT regexp_like('aaaaaaaaaaaaaaaaaaaaaaaab', '^a+b$');  -- Safe
```

### Input Validation

```sql
-- Always validate user input patterns
CREATE OR REPLACE FUNCTION safe_regex_match(input_text text, user_pattern text)
RETURNS boolean AS $$
BEGIN
    -- Validate pattern length
    IF length(user_pattern) > 100 THEN
        RAISE EXCEPTION 'Pattern too long';
    END IF;
    
    -- Check for dangerous patterns
    IF user_pattern ~ '(\+\+|\*\*|\{\d+,\})' THEN
        RAISE EXCEPTION 'Potentially dangerous pattern';
    END IF;
    
    -- Set statement timeout
    SET statement_timeout = '5s';
    
    RETURN regexp_like(input_text, user_pattern);
EXCEPTION
    WHEN OTHERS THEN
        RESET statement_timeout;
        RETURN false;
END;
$$ LANGUAGE plpgsql;
```

---

## Detailed Function Reference

### `substring()` with Regex

```sql
-- Extract substring matching pattern
SELECT substring('foobar' from 'o.b');     -- oob

-- With capturing groups (returns first group)
SELECT substring('foobar' from 'o(.)b');   -- o

-- SIMILAR TO syntax
SELECT substring('abc123def' similar '%#"[0-9]+#"%' escape '#');  -- 123
```

### `regexp_instr()` - Find Position

```sql
-- Find starting position of match
SELECT regexp_instr('number of your street, town zip', '[^,]+', 1, 2);  -- 23

-- Find ending position
SELECT regexp_instr('ABCDEFGHI', '(c..)(...)', 1, 1, 1, 'i', 2);       -- 6
```

### `regexp_substr()` - Extract Substring

```sql
-- Extract matching substring (PostgreSQL 15+)
SELECT regexp_substr('number of your street, town zip', '[^,]+', 1, 2);
-- Result: " town zip"

-- With subexpression
SELECT regexp_substr('ABCDEFGHI', '(c..)(...)', 1, 1, 'i', 2);
-- Result: "FGH"
```

---

## Pattern Syntax

### Anchors

| Anchor | Description | Example |
|--------|-------------|---------|
| `^` | Start of string/line | `^Hello` matches "Hello World" |
| `$` | End of string/line | `World$` matches "Hello World" |
| `\A` | Start of string only | Similar to `^` but string-only |
| `\Z` | End of string only | Similar to `$` but string-only |
| `\b` | Word boundary | `\btest\b` matches "test" but not "testing" |
| `\B` | Non-word boundary | `\Btest\B` matches "contest" |

### Special Characters

| Character | Description | Escape |
|-----------|-------------|--------|
| `.` | Any character (except newline) | `\.` |
| `*` | Zero or more quantifier | `\*` |
| `+` | One or more quantifier | `\+` |
| `?` | Zero or one quantifier | `\?` |
| `|` | Alternation (OR) | `\|` |
| `()` | Grouping | `\(\)` |
| `[]` | Character class | `\[\]` |
| `{}` | Quantifier braces | `\{\}` |
| `^` | Start anchor | `\^` |
| `$` | End anchor | `\$` |
| `\` | Escape character | `\\` |

---

## Examples and Use Cases

### Data Validation

```sql
-- Credit card number validation (basic)
SELECT regexp_like('4111-1111-1111-1111', '^\d{4}-\d{4}-\d{4}-\d{4}$');

-- Social Security Number
SELECT regexp_like('123-45-6789', '^\d{3}-\d{2}-\d{4}$');

-- ZIP code (US)
SELECT regexp_like('12345-6789', '^\d{5}(-\d{4})?$');

-- IP Address validation
SELECT regexp_like(
    '192.168.1.1',
    '^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
);
```

### Data Cleaning

```sql
-- Remove extra whitespace
SELECT regexp_replace('  hello    world  ', '\s+', ' ', 'g');  -- " hello world "
SELECT trim(regexp_replace('  hello    world  ', '\s+', ' ', 'g'));  -- "hello world"

-- Extract numbers from mixed text
SELECT regexp_replace('Price: $123.45 (was $150.00)', '[^\d.]', '', 'g');  -- "123.45150.00"

-- Clean phone numbers
SELECT regexp_replace('(555) 123-4567 ext. 890', '[^\d]', '', 'g');  -- "5551234567890"

-- Normalize case
UPDATE users SET email = LOWER(email) WHERE email ~ '[A-Z]';
```

### Text Processing

```sql
-- Convert CamelCase to snake_case
SELECT regexp_replace(
    regexp_replace('CamelCaseString', '([a-z])([A-Z])', '\1_\2', 'g'),
    '([A-Z])', '\L\1', 'g'
);  -- "camel_case_string"

-- Extract hashtags from social media text
SELECT regexp_matches(
    'Great day! #sunny #weekend #fun #coding',
    '#(\w+)',
    'g'
);

-- Parse log entries
SELECT regexp_match(
    '2024-08-14 10:30:45 [ERROR] Database connection failed',
    '(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.*)'
);
-- Result: {2024-08-14,10:30:45,ERROR,Database connection failed}
```

### Advanced Text Analysis

```sql
-- Word frequency analysis
WITH words AS (
    SELECT regexp_split_to_table(
        lower(regexp_replace(content, '[^\w\s]', '', 'g')),
        '\s+'
    ) AS word
    FROM articles
    WHERE word != ''
)
SELECT word, count(*) as frequency
FROM words
GROUP BY word
ORDER BY frequency DESC;

-- Extract mentions from text
SELECT regexp_matches(
    'Thanks @john and @mary for the help!',
    '@(\w+)',
    'g'
) AS mentions;

-- Find duplicated words
SELECT regexp_matches(
    'This is is a test test sentence',
    '\b(\w+)\s+\1\b',
    'gi'
) AS duplicates;
```

---

*This comprehensive guide covers PostgreSQL's powerful POSIX regular expression capabilities. Regular expressions are a powerful tool, but remember to consider performance implications and security concerns when using them in production applications.*
