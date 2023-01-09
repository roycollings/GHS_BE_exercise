# Using my solution
An example query containing all possible fields:
```graphql
query Query {
	management {
		trades(filter: { baseSymbol: "MATIC" }, page: { number: 3, size: 25 }) {
			totalCount
			trades {
				user {
					username
				}

				base {
					symbol
				}
				amount

				quote {
					symbol
				}
				price

				fee {
					currency {
						symbol
						name
					}
					amount
				}

				placedAt

				labels {
					key {
						name
					}
					value
				}
			}
		}
	}
}

```

# Project Setup

## Prerequisites
Install the following tools:
- make
- Python 3.10
- docker-compose to initialize and run the database

## Installation

Install the application dependencies:
```shell
make init
```

## Usage

1. Start the database:
    ```shell
    docker-compose up -d
    ```

2. Start the application in the development mode:
    ```shell
    make run
    ```

After executing the last command, application should start up and expose api at: <http://localhost:8080/graphql>
