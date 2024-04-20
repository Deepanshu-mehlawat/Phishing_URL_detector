from urllib.parse import urlparse

def extract_features_from_url(url):
    parsed_url = urlparse(url)

    # Initialize feature dictionary
    features = {
        'NumDots': url.count('.'),
        'SubdomainLevel': len(parsed_url.netloc.split('.')) - 1,
        'PathLevel': len(parsed_url.path.split('/')) - 1,
        'UrlLength': len(url),
        'NumDash': url.count('-'),
        'NumDashInHostname': parsed_url.netloc.count('-'),
        'AtSymbol': '@' in parsed_url.netloc,
        'TildeSymbol': '~' in url,
        'NumUnderscore': url.count('_'),
        'NumPercent': url.count('%'),
        'NumQueryComponents': len(parsed_url.query.split('&')),
        'NumAmpersand': url.count('&'),
        'NumHash': url.count('#'),
        'NumNumericChars': sum(c.isdigit() for c in url),
        'NoHttps': 1 if parsed_url.scheme != 'https' else 0,
        'RandomString': 1 if len(parsed_url.query) > 0 and '=' not in parsed_url.query else 0,
        'IpAddress': 1 if parsed_url.netloc.replace('.', '').isdigit() else 0,
        'DomainInSubdomains': parsed_url.netloc.count('.') > 1,
        'DomainInPaths': parsed_url.netloc in parsed_url.path,
        'HttpsInHostname': 'https' in parsed_url.netloc,
        'HostnameLength': len(parsed_url.netloc),
        'PathLength': len(parsed_url.path),
        'QueryLength': len(parsed_url.query),
        'DoubleSlashInPath': '//' in parsed_url.path
    }

    return features
