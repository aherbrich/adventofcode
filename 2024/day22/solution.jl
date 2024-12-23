struct Solution
end

function readFile(filename::String)
    nums = Int[]
    for line in eachline(filename)
        push!(nums, parse(Int, strip(line)))
    end
    return nums
end

function evolveSecretNum(num::Int)
    num = num ⊻ (num * 64)
    num = num % 16777216

    num = num ⊻ (num ÷ 32)
    num = num % 16777216

    num = num ⊻ (num * 2048)
    num = num % 16777216

    return num
end

function solution1(filename::String)
    nums = readFile(filename)

    res = 0
    for num in nums
        for _ in 1:2000
            num = evolveSecretNum(num)
        end
        res += num
    end

    return res
end

function solution2(filename::String)
    nums = readFile(filename)

    bananas = [Int[] for _ in 1:length(nums)]
    deltas = [Int[] for _ in 1:length(nums)]
    
    for (i, num) in pairs(nums)
        last_digit = num % 10
        for _ in 1:2000
            num = evolveSecretNum(num)
            push!(bananas[i], num % 10)
            push!(deltas[i], (num % 10) - last_digit)
            last_digit = num % 10
        end
    end

    maxi = 0
    best_seq = []
    for a in -9:9, b in -9:9, c in -9:9, d in -9:9
        seq = [a, b, c, d]
        
        res = 0
        for k in 1:length(nums)
            for i in 1:(length(bananas[k]) - 3)
                match = true
                for j in 1:4
                    if deltas[k][i+j-1] != seq[j]
                        match = false
                        break
                    end
                end
                
                if match
                    res += bananas[k][i+3]
                    break
                end

            end
        end

        if res > maxi
            best_seq = seq
        end

        maxi = max(maxi, res)

        # println("($a, $b, $c, $d) = $maxi seq = $best_seq")
    end

    return maxi, best_seq
end

# Example usage:
println(solution1("/Users/aherbrich/src/myprojects/adventofcode24/2024/day22/input.txt"))
println(solution2("/Users/aherbrich/src/myprojects/adventofcode24/2024/day22/input.txt"))
