# PostgreSQL Data Types

PostgreSQL offers a rich variety of built-in data types. Understanding these types is crucial for proper database design and optimization.

## Numeric Types

| Type | Description | Size | Range |
|------|-------------|------|-------|
| SMALLINT | Small-range integer | 2 bytes | -32,768 to +32,767 |
| INTEGER | Typical choice for integers | 4 bytes | -2,147,483,648 to +2,147,483,647 |
| BIGINT | Large-range integer | 8 bytes | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| DECIMAL | User-specified precision | variable | Up to 131,072 digits before decimal; up to 16,383 after |
| NUMERIC | User-specified precision | variable | Up to 131,072 digits before decimal; up to 16,383 after |
| REAL | Variable-precision | 4 bytes | 6 decimal digits precision |
| DOUBLE PRECISION | Variable-precision | 8 bytes | 15 decimal digits precision |
| SERIAL | Auto-incrementing integer | 4 bytes | 1 to 2,147,483,647 |
| BIGSERIAL | Auto-incrementing big integer | 8 bytes | 1 to 9,223,372,036,854,775,807 |

## Character Types

| Type | Description |
|------|-------------|
| CHAR(n) | Fixed-length, blank padded |
| VARCHAR(n) | Variable-length with limit |
| TEXT | Variable unlimited length |

## Example Usage

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price NUMERIC(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_available BOOLEAN DEFAULT TRUE,
    tags TEXT[],
    metadata JSONB
);

-- Insert with different data types
INSERT INTO products (name, description, price, is_available, tags, metadata)
VALUES (
    'Ergonomic Chair',
    'Comfortable office chair with lumbar support',
    199.99,
    true,
    ARRAY['furniture', 'office', 'ergonomic'],
    '{"color": "black", "dimensions": {"height": 120, "width": 65, "depth": 70}, "materials": ["leather", "metal"]}'
);
```