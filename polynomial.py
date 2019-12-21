class Polynomial:
    def __init__(self, *coefficients):
        self.coef = []
        if isinstance(coefficients[0], list):
            self.coef = coefficients[0]
        elif isinstance(coefficients[0], dict):
            self.coef = [0 for i in range(max(coefficients[0]) + 1)]
            for power in coefficients[0]:
                self.coef[power] = coefficients[0][power]
        elif isinstance(coefficients[0], Polynomial):
            self.coef = coefficients[0].coef
        else:
            for coef in coefficients:
                self.coef.append(coef)

        for i in range(len(self.coef) - 1, -1, -1):
            if self.coef[i] == 0:
                self.coef.pop()
            else:
                break

    def __repr__(self):
        return "Polynomial " + str(self.coef)

    def degree(self):
        deg = len(self.coef)
        if deg == 0:
            return deg
        else:
            return deg - 1

    def __str__(self):
        res = ''
        deg = self.degree()
        max_deg = self.degree()
        if len(self.coef) == 0:
            return '0'
        else:
            while deg >= 0:
                coeff = int(self.coef[deg])
                if deg == 1:
                    if coeff == 1:
                        res += '+ ' + 'x' + ' '
                    elif coeff == -1:
                        res += '- ' + 'x' + ' '
                    elif coeff != 0:
                        if coeff > 0:
                            res += '+ ' + str(abs(coeff)) + 'x' + ' '
                        else:
                            res += '- ' + str(abs(coeff)) + 'x' + ' '
                elif deg == 0:
                    if coeff != 0:
                        if coeff > 0:
                            res += '+ ' + str(abs(coeff)) + ' '
                        else:
                            res += '- ' + str(abs(coeff)) + ' '
                else:
                    if coeff == 1:
                        res +=  'x^' + str(deg) + ' '
                    elif coeff == -1:
                        res += '- ' + 'x^' + str(deg) + ' '
                    elif coeff != 0:
                        if coeff > 0:
                            res += '+ ' + str(abs(coeff)) + 'x^' + str(deg) + ' '
                        else:
                            res += '- ' + str(abs(coeff)) + 'x^' + str(deg) + ' '
                deg -= 1
            if res[0] == '+':
                return res[2:-1]
            else:
                return '-' + res[2:-1]

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coef == other.coef
        else:
            if other == 0:
                return len(self.coef) == 0
            else:
                return len(self.coef) == 1 and self.coef[0] == other

    def __add__(self, other):
        res = []
        self = Polynomial(self)
        other = Polynomial(other)
        min_len = min(len(self.coef), len(other.coef))
        max_len = max(len(self.coef), len(other.coef))
        for i in range(min_len):
            res.append(self.coef[i] + other.coef[i])
        if max_len > min_len and max_len == len(self.coef):
            for j in range(min_len, max_len):
                res.append(self.coef[j])
        elif max_len > min_len and max_len == len(other.coef):
            for j in range(min_len, max_len):
                res.append(other.coef[j])
        return Polynomial(res)
            
    def __radd__(self, other):
        res = []
        self = Polynomial(self)
        other = Polynomial(other)
        min_len = min(len(self.coef), len(other.coef))
        max_len = max(len(self.coef), len(other.coef))
        for i in range(min_len):
            res.append(self.coef[i] + other.coef[i])
        if max_len > min_len and max_len == len(self.coef):
            for j in range(min_len, max_len):
                res.append(self.coef[j])
        elif max_len > min_len and max_len == len(other.coef):
            for j in range(min_len, max_len):
                res.append(other.coef[j])
        return Polynomial(res)
    
    def __neg__(self):
        for i in range(len(self.coef)):
            self.coef[i] *= -1
        return self
    
    def __sub__(self, other):
        return self + (-other)
    
    def __rsub__(self, other):
        return (- self) + other
    
    def __call__(self, x):
        deg = self.degree()
        res = self.coef[0]
        for i in range(1, deg + 1):
            res += self.coef[i] * (x ** i) 
        return res
        
    def der(self, d=1):
        deg = self.degree()
        res = []
        for i in range(1, deg + 1):
            res.append(self.coef[i] * i)
        res = Polynomial(res) 
        if d == 1:
            return res
        elif d == 0:
            return self
        else:
            return res.der(d - 1)
        
    def __mul__(self, other):
        self = Polynomial(self)
        other = Polynomial(other)
        if other.degree() > self.degree():
            self1 = other
            other1 = self
        else:
            self1 = self
            other1 = other
        res = [0 for i in range(self.degree() + other.degree() + 1)]
        for i in range(len(res)):
            for j in range(max(0, i - other1.degree()), min(self1.degree() + 1, i + 1)):
                res[i] += self1.coef[j] * other1.coef[i - j]
        return Polynomial(res)
    
    def __rmul__(self, other):
        return other * self    
    
    def __mod__(self, other):
        pass
    def __rmod__(self, other):
        pass
    def gcd(self, other):
        pass
    def __iter__(self):
        self.iter = 0
        return self
 
    def __next__(self):
        if self.iter == len(self.coef):
            raise StopIteration
        else:
            result = (self.iter, self.coef[self.iter])
            self.iter += 1
            return result

class RealPolynomial(Polynomial):
    def find_root(self):
        pass

class QuadraticPolynomial(Polynomial):
    def solve(self):
        a, b, c = self.coef[2], self.coef[1], self.coef[0]
        D = b ** 2 - 4 * a * c
        if D < 0:
            return []
        elif D == 0:
            return [- b / (2 * a)]
        else:
            return [(D ** 0.5 - b) / (2 * a), (- D ** 0.5 - b) / (2 * a)]

