store = {}
store['timestamp']=1620914561
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=12']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=12
store['worker_id']=12
store['num_workers']=20
store['config']={'seed': 1252, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.370654582977295})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.535623550415039})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.824517250061035})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.7592058181762695})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6903, 'crossentropy': 2.0846482421875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.139554500579834})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1397349834442139})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0954222679138184})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [49561, 25051, 979, 50159, 3148, 34718, 47452, 903, 16540, 37626], 'labels': [0, 0, 0, 6, 8, 2, 0, 0, 0, 3], 'scores': [0.957243025302887, 0.6376377940177917, 1.0217931270599365, 0.7934133410453796, 0.652286946773529, 0.8910462856292725, 0.9539228081703186, 0.9680384993553162, 0.8536539077758789, 0.6512879133224487]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.782585859298706})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.5116639137268066})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.602536678314209})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.685335636138916})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7242, 'crossentropy': 1.8106462890625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0343520641326904})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9786993265151978})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9792271852493286})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [20261, 1485, 37902, 12173, 34649, 29989, 30782, 17165, 28341, 13417], 'labels': [8, 5, -1, 8, 8, 8, 9, 8, 8, -1], 'scores': [0.7533972859382629, 0.8410643339157104, 0.42081451416015625, 0.5770208239555359, 0.7311794757843018, 0.7139354944229126, 0.8419893383979797, 0.6885056495666504, 0.8382629156112671, 0.6045233011245728]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8809235095977783})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.9974567890167236})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.3294601440429688})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.4081807136535645})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7188, 'crossentropy': 1.6902068359375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1604890823364258})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0425745248794556})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0773627758026123})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [1883, 3039, 40109, 19287, 12869, 12188, 1376, 55773, 17987, 51947], 'labels': [3, 4, 3, 4, -1, 7, 7, 4, -1, 3], 'scores': [0.6074535250663757, 0.5909466743469238, 0.6387996077537537, 0.6950544118881226, 0.4506469964981079, 0.5186125636100769, 0.5392156839370728, 0.6857253313064575, 0.3073359727859497, 0.5409293174743652]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.4192801713943481})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.4907701015472412})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.6050641536712646})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.608837366104126})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.772, 'crossentropy': 1.28965556640625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.9984030723571777})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.9293237924575806})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.8599593639373779})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [14084, 52498, 26511, 53517, 4853, 47753, 23568, 18825, 18370, 16560], 'labels': [2, -1, 6, 8, 8, 8, 5, -1, 2, 6], 'scores': [0.7787943482398987, 0.4822084903717041, 0.7390342950820923, 0.5864684581756592, 0.6504659652709961, 0.7382687926292419, 0.6300657391548157, 0.3163309097290039, 0.5905634164810181, 0.5834093689918518]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.2558631896972656})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.427801489830017})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.5137765407562256})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.4381299018859863})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8071, 'crossentropy': 1.1469171875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.8873355388641357})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.8650919795036316})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8150867819786072})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [40818, 48100, 40972, 50469, 20600, 56104, 30932, 39504, 47221, 7669], 'labels': [-1, 7, 5, 6, 7, -1, 0, -1, 7, -1], 'scores': [0.49516284465789795, 0.5038669109344482, 0.6083559989929199, 0.5552819967269897, 0.6680729389190674, 0.30179381370544434, 0.6963788866996765, 0.4132053852081299, 0.4496781826019287, 0.5089739561080933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.325302004814148})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.4299654960632324})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.572314977645874})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.7284424304962158})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.791, 'crossentropy': 1.27315986328125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.8875000476837158})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.8456104397773743})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.7998168468475342})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [47781, 22824, 35622, 22517, 11410, 54889, 22366, 4701, 10811, 59325], 'labels': [3, 9, 3, 5, 5, 8, 3, 2, 5, 9], 'scores': [0.7333787083625793, 0.6898632645606995, 0.5454348921775818, 0.521328330039978, 0.6748749017715454, 0.4901657700538635, 0.6539204716682434, 0.5519161820411682, 0.6634154915809631, 0.406355619430542]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9796837568283081})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2077993154525757})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.3230817317962646})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.5075535774230957})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8293, 'crossentropy': 0.93730888671875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8721956014633179})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.7671379446983337})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7799155712127686})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [54965, 10473, 27430, 53029, 38733, 43978, 20299, 49021, 13395, 56412], 'labels': [9, 6, 9, 2, 2, 3, 2, 2, 9, 8], 'scores': [0.34336113929748535, 0.3603811264038086, 0.43824368715286255, 0.4080162048339844, 0.4639433026313782, 0.5044890642166138, 0.4987948536872864, 0.39256858825683594, 0.33578890562057495, 0.4208688735961914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9032277464866638})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0322964191436768})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0997161865234375})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1869186162948608})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8263, 'crossentropy': 0.93542763671875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8537302017211914})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7303716540336609})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7357943058013916})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [31253, 13107, 19748, 53201, 45122, 12157, 35178, 8569, 48606, 5970], 'labels': [5, 1, 9, 5, 8, 5, 4, 5, 5, 3], 'scores': [0.5604903697967529, 0.5082438588142395, 0.38181072473526, 0.5724685192108154, 0.5069124698638916, 0.6640583276748657, 0.40488576889038086, 0.5733886957168579, 0.5250077247619629, 0.3620592951774597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8850131034851074})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.858596682548523})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9425889253616333})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9513905644416809})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8987122774124146})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8793, 'crossentropy': 0.74627109375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.669784665107727})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6062440276145935})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5607900619506836})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5164401531219482})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [42828, 42702, 58809, 17535, 26457, 57415, 21336, 15694, 6097, 8825], 'labels': [7, 1, 0, 0, 0, -1, -1, 0, 0, 4], 'scores': [0.5943524837493896, 0.4879952073097229, 0.7494249939918518, 0.7026457786560059, 0.44379952549934387, 0.5078026652336121, 0.4948352575302124, 0.7480058670043945, 0.7866617441177368, 0.5659928917884827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9537016153335571})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9407253861427307})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9464385509490967})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.000551462173462})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9451606273651123})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8728, 'crossentropy': 0.8119509765625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7475056648254395})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.688058078289032})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6138796806335449})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6251582503318787})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [36029, 30673, 6846, 4058, 43126, 21315, 17129, 5198, 33141, 45349], 'labels': [-1, -1, -1, 8, 3, 8, 1, 4, 9, -1], 'scores': [0.4357820749282837, 0.3956226110458374, 0.44994795322418213, 0.5965015292167664, 0.4400603771209717, 0.6962614059448242, 0.5500128865242004, 0.5895490050315857, 0.6125967502593994, 0.24092960357666016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8425953388214111})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7779457569122314})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7754063606262207})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8537535667419434})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.810786247253418})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8063308000564575})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9105, 'crossentropy': 0.680634423828125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7514464855194092})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5382792353630066})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5662028193473816})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5260404348373413})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5154296159744263})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [13945, 3070, 7891, 29255, 14413, 5106, 45380, 22235, 14665, 14647], 'labels': [9, 1, 8, -1, 8, 9, 9, -1, 8, 9], 'scores': [0.42403924465179443, 0.6778161525726318, 0.5651300549507141, 0.5654031038284302, 0.5005786418914795, 0.6052774786949158, 0.5977967977523804, 0.23726987838745117, 0.27986010909080505, 0.5350632667541504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9235415458679199})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8293641805648804})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8101892471313477})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8612223863601685})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9172216653823853})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9062886834144592})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.682044580078125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6824823617935181})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.550764799118042})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5046805143356323})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.49275872111320496})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5084251165390015})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [44674, 22579, 50294, 31312, 44901, 37440, 22083, 33784, 22182, 2706], 'labels': [5, 2, 6, 9, 2, 2, 2, 9, 3, 7], 'scores': [0.4806802272796631, 0.4549906849861145, 0.644109845161438, 0.4968975782394409, 0.44342488050460815, 0.6211448907852173, 0.5853052735328674, 0.4118388593196869, 0.4280351400375366, 0.5992057919502258]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.929112434387207})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7356581687927246})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7595883011817932})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8798028230667114})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.934701681137085})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9015, 'crossentropy': 0.6112990234375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7765089869499207})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6318097114562988})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5624808669090271})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5791676044464111})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [43234, 15849, 11621, 11482, 39546, 34800, 24479, 47597, 48504, 1298], 'labels': [8, 7, 2, 8, 1, 5, 8, 8, 9, 5], 'scores': [0.36556142568588257, 0.31948113441467285, 0.5235865712165833, 0.5453581809997559, 0.35681021213531494, 0.41149747371673584, 0.5098076462745667, 0.5691947937011719, 0.3840690851211548, 0.320819616317749]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8849376440048218})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7220264673233032})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.737758994102478})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7569789886474609})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8067311644554138})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8914, 'crossentropy': 0.667222802734375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6969664096832275})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6110734939575195})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5261378288269043})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.5222530364990234})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [18037, 23104, 20110, 30123, 25234, 59287, 35533, 13003, 33296, 53993], 'labels': [7, 0, 4, 0, 4, 9, 4, -1, 2, 6], 'scores': [0.5912200808525085, 0.45838481187820435, 0.5857986211776733, 0.4915391206741333, 0.42697256803512573, 0.4198707342147827, 0.536579966545105, 0.45385968685150146, 0.4466921091079712, 0.40955573320388794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8235515356063843})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6838304400444031})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7529305219650269})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7415979504585266})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7815808057785034})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8898, 'crossentropy': 0.622922216796875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7930784225463867})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.5941773653030396})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5744792222976685})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5981578826904297})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [40547, 47140, 35411, 54814, 29839, 13781, 26292, 28757, 51394, 1254], 'labels': [8, 3, 6, 4, 2, 8, 0, 3, 8, -1], 'scores': [0.48503291606903076, 0.3420306444168091, 0.326016902923584, 0.40250182151794434, 0.4540640711784363, 0.45124149322509766, 0.37857961654663086, 0.4671757221221924, 0.3428022861480713, 0.5754660367965698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9053831100463867})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6911443471908569})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6446740627288818})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6787629723548889})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6600607633590698})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7262883186340332})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9139, 'crossentropy': 0.59272919921875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7608017921447754})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5165213942527771})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.535137414932251})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4936255216598511})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.44692593812942505})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [40418, 55428, 54768, 52775, 33198, 4043, 25117, 39952, 52582, 8501], 'labels': [-1, 5, -1, -1, 8, -1, -1, 5, 2, -1], 'scores': [0.435299277305603, 0.5403745174407959, 0.44249439239501953, 0.3763469457626343, 0.6162586808204651, 0.7077062129974365, 0.4839479923248291, 0.7189761400222778, 0.6534203886985779, 0.47743308544158936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8529998064041138})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6708165407180786})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6403900384902954})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7324020862579346})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.596255898475647})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6699773073196411})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6614998579025269})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6698471307754517})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9233, 'crossentropy': 0.593806591796875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7649716734886169})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5457670092582703})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4726880192756653})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4612574577331543})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.43289679288864136})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.40662527084350586})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.41931337118148804})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [3517, 23840, 50153, 51392, 8458, 22256, 48975, 39469, 26618, 18242], 'labels': [-1, -1, -1, -1, 4, -1, 2, -1, -1, -1], 'scores': [0.5189008116722107, 0.7019103169441223, 0.44911742210388184, 0.43807244300842285, 0.5833990573883057, 0.4307420253753662, 0.5593141317367554, 0.4926801323890686, 0.5327982306480408, 0.5468278527259827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8712601065635681})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6476155519485474})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.612221360206604})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5941607356071472})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6659591197967529})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6434634923934937})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6689767837524414})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.56412724609375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6845528483390808})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5131849050521851})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4645025134086609})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43095606565475464})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.41550496220588684})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.40836960077285767})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [42509, 58471, 15119, 28455, 52938, 29182, 6291, 29018, 25719, 36016], 'labels': [5, -1, -1, 5, 2, 3, 3, -1, -1, -1], 'scores': [0.5918325781822205, 0.44608622789382935, 0.5872073173522949, 0.6731687784194946, 0.4548533260822296, 0.6157497763633728, 0.46078646183013916, 0.545658141374588, 0.4299728274345398, 0.43979984521865845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9600047469139099})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6307051777839661})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5661433935165405})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6983659267425537})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6162242889404297})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7247434854507446})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.542911962890625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7032536864280701})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5708906650543213})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.46071314811706543})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.47078195214271545})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4319759011268616})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [21433, 26034, 28781, 21608, 56286, 43856, 33356, 6650, 14701, 131], 'labels': [5, 5, 7, 0, 8, 5, -1, 7, -1, -1], 'scores': [0.47686851024627686, 0.49648046493530273, 0.4751524329185486, 0.47225016355514526, 0.41128969192504883, 0.6434114575386047, 0.5577251315116882, 0.48333871364593506, 0.5343958139419556, 0.5605257153511047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9384548664093018})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6933251023292542})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6568593382835388})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7611551284790039})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6269903779029846})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6952673196792603})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7175869941711426})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6586142182350159})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9043, 'crossentropy': 0.63041162109375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7400264739990234})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.5881079435348511})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.45481210947036743})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.47163569927215576})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.44094353914260864})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.42426425218582153})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4096410274505615})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [47840, 5293, 49859, 47068, 12817, 12767, 49336, 42565, 35025, 36392], 'labels': [6, 4, 3, 4, 4, 9, -1, -1, -1, 9], 'scores': [0.41628625988960266, 0.4409397840499878, 0.6659975647926331, 0.463370144367218, 0.549952507019043, 0.3408377468585968, 0.44722288846969604, 0.4665837287902832, 0.36876773834228516, 0.3768343925476074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8318779468536377})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5652569532394409})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5477203130722046})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5445442199707031})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5531960725784302})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49978962540626526})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5517101287841797})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5628408193588257})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6192841529846191})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.479299658203125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6874006986618042})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.48454898595809937})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.43690773844718933})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.368621289730072})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3975852131843567})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3619263470172882})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3619595170021057})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3492852449417114})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [8847, 22895, 3454, 53478, 20072, 48053, 23991, 9926, 34542, 41770], 'labels': [9, 9, 6, 7, 3, -1, -1, 6, 1, 0], 'scores': [0.5894100069999695, 0.4192310571670532, 0.35848450660705566, 0.40437257289886475, 0.5477541089057922, 0.25023698806762695, 0.35312461853027344, 0.5413008332252502, 0.46900975704193115, 0.37686723470687866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.880617618560791})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.603318452835083})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.543285608291626})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5504055619239807})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5019898414611816})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6103527545928955})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5484990477561951})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5336136817932129})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9393, 'crossentropy': 0.462754345703125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7201476097106934})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4827228784561157})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.40205323696136475})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4111444354057312})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.40209895372390747})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37494510412216187})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.379675030708313})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [20635, 12593, 17265, 9158, 9119, 37087, 27435, 9428, 57972, 13516], 'labels': [5, 3, 2, 0, 9, 4, 3, 9, 4, 3], 'scores': [0.4631481468677521, 0.5419473052024841, 0.6979086399078369, 0.621387779712677, 0.4511587619781494, 0.5152941942214966, 0.42460861802101135, 0.4445929229259491, 0.5146623253822327, 0.6136810779571533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9112600088119507})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6238875389099121})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6414520740509033})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.526700496673584})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5321825742721558})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.556973934173584})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6462690830230713})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9431, 'crossentropy': 0.4398208984375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6958884000778198})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4989481568336487})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42638689279556274})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.401887446641922})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3895513415336609})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3522619605064392})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [2546, 3386, 31889, 55132, 1737, 45069, 37713, 15055, 51231, 32427], 'labels': [4, -1, -1, -1, -1, 4, -1, -1, 5, 0], 'scores': [0.4003046751022339, 0.4141853451728821, 0.5220903158187866, 0.37177205085754395, 0.3868682384490967, 0.3927918076515198, 0.3707156777381897, 0.37664514780044556, 0.5622013211250305, 0.6084229350090027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0029817819595337})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5532475113868713})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5206494331359863})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5726634860038757})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.586192786693573})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6028368473052979})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.466109619140625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.77348792552948})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.533010721206665})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.48763567209243774})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4593461751937866})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.461953729391098})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [659, 20287, 35132, 2202, 14290, 44948, 22163, 6443, 26326, 19855], 'labels': [3, 4, -1, 1, 4, 9, -1, -1, -1, 3], 'scores': [0.6311138272285461, 0.4186984598636627, 0.3278660774230957, 0.40560585260391235, 0.5756608247756958, 0.530504047870636, 0.3397092819213867, 0.28265994787216187, 0.3177706003189087, 0.5863854289054871]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.803870677947998})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5273549556732178})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.49850860238075256})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5424485802650452})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.496038019657135})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4621645212173462})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5147438645362854})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49274903535842896})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5447525978088379})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9455, 'crossentropy': 0.42244677734375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.714413583278656})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.47808367013931274})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.405767023563385})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.37462127208709717})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.38982415199279785})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3575775921344757})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3485945165157318})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3347409665584564})
store['active_learning_steps'][24]['eval_training']['best_epoch']=8
store['active_learning_steps'][24]['acquisition']={'indices': [35168, 57244, 7244, 30075, 29754, 26087, 2740, 28178, 22265, 46523], 'labels': [-1, -1, -1, -1, -1, -1, -1, 5, -1, -1], 'scores': [0.5176527500152588, 0.4439014196395874, 0.4757087230682373, 0.46187031269073486, 0.35532641410827637, 0.42851197719573975, 0.5081460475921631, 0.41304630041122437, 0.36809349060058594, 0.45049500465393066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9751455187797546})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5460605621337891})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5065749883651733})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5022081136703491})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5230718851089478})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.535552978515625})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5616140365600586})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9424, 'crossentropy': 0.43192529296875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7257669568061829})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4827311038970947})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4420351982116699})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3939443528652191})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.39113491773605347})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3720136880874634})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [57195, 52854, 51285, 23841, 23588, 5129, 37397, 20265, 48040, 21990], 'labels': [3, 1, 1, 1, 7, 2, 3, 2, -1, 1], 'scores': [0.5346044301986694, 0.4855262041091919, 0.24484920501708984, 0.32168322801589966, 0.4483490586280823, 0.6598957180976868, 0.6253196001052856, 0.3218153119087219, 0.40795373916625977, 0.5167531967163086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.849799633026123})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.50669264793396})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47269606590270996})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4651457667350769})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49889546632766724})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5037078857421875})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5402539372444153})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9418, 'crossentropy': 0.4221896484375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7826424241065979})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.472748339176178})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4562406539916992})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3659563660621643})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.35951972007751465})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3417234420776367})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [31344, 13604, 27381, 27576, 8351, 57728, 17190, 45424, 16951, 33278], 'labels': [-1, 1, 8, 5, 1, 9, 9, 4, 8, -1], 'scores': [0.27775120735168457, 0.6826359629631042, 0.3062177896499634, 0.43622392416000366, 0.39628130197525024, 0.5394566059112549, 0.3588981032371521, 0.35117974877357483, 0.5355959534645081, 0.21251928806304932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8792577981948853})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5449738502502441})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4998285174369812})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4500305652618408})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4308288097381592})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46558916568756104})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5167479515075684})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4548993706703186})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9483, 'crossentropy': 0.385511083984375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7243324518203735})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4565024971961975})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.36776649951934814})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36419278383255005})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.31372612714767456})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3110160529613495})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32651007175445557})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [25498, 44748, 28507, 7868, 24325, 18294, 16035, 3694, 43247, 5259], 'labels': [4, 8, -1, -1, -1, -1, 9, -1, -1, 2], 'scores': [0.6548819541931152, 0.6135923862457275, 0.40989768505096436, 0.3744257688522339, 0.42392730712890625, 0.4780619144439697, 0.4343971610069275, 0.39863741397857666, 0.44787144660949707, 0.5035578608512878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8472181558609009})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5497667789459229})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4181969165802002})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46914994716644287})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42134785652160645})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4682609736919403})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9492, 'crossentropy': 0.3879196044921875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6948845386505127})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.46049556136131287})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4049113392829895})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39321422576904297})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39617985486984253})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [4752, 19771, 28317, 15332, 46566, 18550, 28368, 44011, 7981, 38624], 'labels': [-1, -1, -1, 3, 3, -1, 9, -1, -1, -1], 'scores': [0.3898576498031616, 0.47845298051834106, 0.43840491771698, 0.47797441482543945, 0.3574351966381073, 0.363034725189209, 0.6842747330665588, 0.40952908992767334, 0.36164939403533936, 0.4176223874092102]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.94987952709198})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5123907327651978})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4520595073699951})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4429900348186493})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41111019253730774})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41552966833114624})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43263185024261475})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4749950170516968})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9495, 'crossentropy': 0.356929296875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7723684310913086})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5330124497413635})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.41299498081207275})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.38286101818084717})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3415025472640991})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3349788784980774})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33516883850097656})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [9568, 26185, 29736, 45478, 10275, 53643, 57213, 39208, 24630, 3629], 'labels': [5, -1, -1, 6, 6, -1, -1, 5, 5, -1], 'scores': [0.49625062942504883, 0.3386809825897217, 0.301336407661438, 0.4196544885635376, 0.4949582815170288, 0.49120593070983887, 0.24037015438079834, 0.5187146663665771, 0.5151309967041016, 0.4179868698120117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9514868259429932})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5275415182113647})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4629005789756775})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4720243215560913})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46596407890319824})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44638121128082275})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49239128828048706})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47672998905181885})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47165295481681824})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9492, 'crossentropy': 0.3882201904296875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6746159195899963})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4590722918510437})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.39688006043434143})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34754958748817444})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.36894309520721436})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.31897932291030884})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.33461838960647583})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3202548623085022})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [51716, 34042, 16511, 10038, 32283, 57402, 28611, 5659, 59449, 26391], 'labels': [-1, 8, 5, 9, -1, -1, 2, 2, -1, 3], 'scores': [0.4000589847564697, 0.39812278747558594, 0.5265701413154602, 0.4577986001968384, 0.28844428062438965, 0.44390034675598145, 0.5753170251846313, 0.534957766532898, 0.2787606716156006, 0.41228175163269043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8707547187805176})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49388587474823})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.42789143323898315})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3812156915664673})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.416864812374115})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46642982959747314})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4316350817680359})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9529, 'crossentropy': 0.351644580078125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6603180766105652})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4937710165977478})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3934333026409149})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.369640976190567})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4064524173736572})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3445276618003845})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [28374, 37489, 55743, 2231, 17082, 34199, 41267, 19590, 50461, 26850], 'labels': [3, 2, 3, 8, 3, -1, 3, 5, 7, 2], 'scores': [0.5150831341743469, 0.45045581459999084, 0.3884117603302002, 0.5452439785003662, 0.5894275307655334, 0.41624945402145386, 0.619280219078064, 0.48247861862182617, 0.4687316417694092, 0.5609282851219177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9316595792770386})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5240057706832886})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.434631884098053})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.437887966632843})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.416114866733551})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4642421007156372})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4577913284301758})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45479831099510193})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9522, 'crossentropy': 0.3757544921875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7573262453079224})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4816654324531555})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3945975601673126})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3874930739402771})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3760342597961426})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31952399015426636})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3182242214679718})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [2297, 4646, 53404, 44385, 20641, 59492, 52186, 59522, 45812, 35443], 'labels': [-1, 2, -1, -1, 9, -1, -1, -1, -1, -1], 'scores': [0.44625693559646606, 0.47858721017837524, 0.16826319694519043, 0.6035829782485962, 0.6289509534835815, 0.4468945264816284, 0.3606506586074829, 0.4205852150917053, 0.4315323233604431, 0.42551732063293457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9991652965545654})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5232224464416504})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44635215401649475})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.405370831489563})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43032824993133545})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39318493008613586})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4064827561378479})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3853934705257416})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42701882123947144})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42304548621177673})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45762571692466736})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9562, 'crossentropy': 0.358267822265625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7123556137084961})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.44189780950546265})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.396823912858963})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3264898955821991})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.31330665946006775})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32032066583633423})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29582834243774414})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.28616100549697876})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2685004472732544})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2922660708427429})
store['active_learning_steps'][33]['eval_training']['best_epoch']=9
store['active_learning_steps'][33]['acquisition']={'indices': [32724, 42321, 30651, 33933, 28966, 19287, 14171, 25624, 26402, 58270], 'labels': [5, 5, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6768070459365845, 0.6840923428535461, 0.3945375680923462, 0.5174082517623901, 0.4805123209953308, 0.45907092094421387, 0.5529729723930359, 0.3726385831832886, 0.37692326307296753, 0.35352492332458496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9209087491035461})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49271705746650696})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.44422006607055664})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.42831501364707947})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.470197856426239})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4565451145172119})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.430574893951416})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9438, 'crossentropy': 0.3910580078125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7092820405960083})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5206563472747803})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4444817900657654})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41491901874542236})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3861742615699768})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.35633713006973267})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [8866, 44255, 30266, 27940, 38820, 5380, 12254, 26718, 38055, 53986], 'labels': [7, 6, 4, -1, -1, -1, 2, 2, 0, 7], 'scores': [0.44922375679016113, 0.5595881938934326, 0.4356916546821594, 0.293365478515625, 0.30995023250579834, 0.20828795433044434, 0.2717735171318054, 0.3661271929740906, 0.4521336555480957, 0.30377158522605896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8849250078201294})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4751129150390625})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38831958174705505})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39668959379196167})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3790302872657776})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40250512957572937})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41289636492729187})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39467930793762207})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9546, 'crossentropy': 0.34632177734375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6914870738983154})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.44552260637283325})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40214812755584717})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36578482389450073})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3364652991294861})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3355870246887207})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31905701756477356})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [3319, 16756, 9787, 20995, 15518, 48160, 29744, 24311, 21381, 10933], 'labels': [-1, 7, -1, -1, 7, -1, 4, 8, -1, -1], 'scores': [0.33123934268951416, 0.5453094840049744, 0.3930553197860718, 0.4425710439682007, 0.3237866163253784, 0.5889718532562256, 0.4932767152786255, 0.4749792218208313, 0.29917430877685547, 0.35903871059417725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0278027057647705})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4908490478992462})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38196760416030884})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3501724898815155})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36034271121025085})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3914109468460083})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3751944899559021})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9551, 'crossentropy': 0.339616650390625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8013362884521484})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4904785752296448})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4058718681335449})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35084640979766846})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37567323446273804})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39528000354766846})
store['active_learning_steps'][36]['eval_training']['best_epoch']=4
store['active_learning_steps'][36]['acquisition']={'indices': [25839, 32393, 50562, 33010, 46189, 11044, 4019, 33338, 53349, 49801], 'labels': [-1, -1, 9, -1, -1, 4, -1, 8, 9, -1], 'scores': [0.3658844828605652, 0.3482682704925537, 0.5986005067825317, 0.5559147000312805, 0.5376811623573303, 0.6234785318374634, 0.5320066213607788, 0.6500231027603149, 0.2754597067832947, 0.4900926947593689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0174705982208252})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5289249420166016})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.493211567401886})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38617879152297974})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41287803649902344})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.424360454082489})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4639149606227875})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9535, 'crossentropy': 0.3678146728515625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7705694437026978})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48299896717071533})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4139470160007477})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35738301277160645})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34229958057403564})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31939175724983215})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [44887, 7768, 45024, 59823, 58649, 1341, 4322, 1518, 16692, 25158], 'labels': [-1, 8, 5, 5, 0, 3, 2, 9, 5, 5], 'scores': [0.3444633483886719, 0.4226672649383545, 0.6055842041969299, 0.47569429874420166, 0.42421823740005493, 0.508154571056366, 0.366197407245636, 0.5444817543029785, 0.5847439765930176, 0.4941730499267578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9524726867675781})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5123643279075623})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3767385482788086})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.382800817489624})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3904181718826294})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3684251606464386})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35076117515563965})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37720149755477905})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4008660316467285})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3974207937717438})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.3265478759765625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7851815819740295})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4869435429573059})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3757990002632141})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32538655400276184})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3171086311340332})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.316811203956604})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30866071581840515})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2886093854904175})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2855391800403595})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
store['active_learning_steps'][38]['acquisition']={'indices': [17237, 56453, 18962, 22203, 26852, 3615, 46179, 54015, 2205, 49580], 'labels': [-1, -1, 7, -1, 8, 6, -1, -1, -1, 2], 'scores': [0.44959747791290283, 0.4045953154563904, 0.41949906945228577, 0.4137216806411743, 0.2971017360687256, 0.596816897392273, 0.37072300910949707, 0.2793712615966797, 0.3293955326080322, 0.4345199465751648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9725439548492432})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47589367628097534})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41798466444015503})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35611599683761597})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3340010344982147})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3367900848388672})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3458377420902252})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3343581557273865})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.3316732666015625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7201215028762817})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42840543389320374})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3744155168533325})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.33496230840682983})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33863574266433716})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3061549663543701})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3176277279853821})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [37219, 2844, 43994, 4594, 32784, 258, 9342, 46820, 31626, 51625], 'labels': [8, -1, -1, -1, 8, -1, -1, -1, 6, -1], 'scores': [0.4314572215080261, 0.5111131072044373, 0.3533679246902466, 0.5693997740745544, 0.5621123313903809, 0.3857921361923218, 0.35262322425842285, 0.35372138023376465, 0.45404526591300964, 0.42343759536743164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8956966400146484})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.47600680589675903})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3889244496822357})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37491199374198914})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3903772234916687})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33864855766296387})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3764030337333679})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37663280963897705})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4110419750213623})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9619, 'crossentropy': 0.3050639404296875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7858464121818542})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5104437470436096})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3736473023891449})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3288812041282654})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3125329911708832})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.26399940252304077})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2965408265590668})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2644572854042053})
store['active_learning_steps'][40]['eval_training']['best_epoch']=6
store['active_learning_steps'][40]['acquisition']={'indices': [48973, 47895, 5216, 38136, 24760, 44100, 16558, 58469, 39647, 51111], 'labels': [8, -1, 2, 8, -1, 4, -1, -1, 8, -1], 'scores': [0.5096166133880615, 0.42245662212371826, 0.3982793688774109, 0.3940569758415222, 0.39762723445892334, 0.4055834412574768, 0.3135387897491455, 0.2960432767868042, 0.24114990234375, 0.25363993644714355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0156116485595703})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5150898694992065})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3818029463291168})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3655484616756439})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35929930210113525})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34186965227127075})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3358932137489319})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32229626178741455})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3569909334182739})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3914399743080139})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3605295419692993})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.2967642333984375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7909937500953674})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4472804069519043})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3795177936553955})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3434118330478668})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30862027406692505})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2960360050201416})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.299372136592865})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2758804261684418})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29526716470718384})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25044363737106323})
store['active_learning_steps'][41]['eval_training']['best_epoch']=10
store['active_learning_steps'][41]['acquisition']={'indices': [21627, 54754, 2591, 17545, 14367, 51984, 28641, 12305, 13, 39888], 'labels': [-1, -1, -1, -1, 3, -1, -1, 9, -1, -1], 'scores': [0.31126540899276733, 0.4042513966560364, 0.6108728647232056, 0.2532779574394226, 0.8078703880310059, 0.4652678966522217, 0.364915132522583, 0.6192762851715088, 0.435467004776001, 0.5038931369781494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0502400398254395})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5919961929321289})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42429158091545105})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34714871644973755})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3542443811893463})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3670048117637634})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35774341225624084})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9586, 'crossentropy': 0.3259743408203125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8257458209991455})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4660595655441284})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42895394563674927})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3500227928161621})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34690165519714355})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31827837228775024})
store['active_learning_steps'][42]['eval_training']['best_epoch']=6
store['active_learning_steps'][42]['acquisition']={'indices': [25909, 5278, 59507, 57221, 31415, 59548, 47885, 22597, 5828, 19702], 'labels': [9, 4, -1, -1, 5, -1, 9, 9, 5, 5], 'scores': [0.4373062252998352, 0.40303486585617065, 0.17580223083496094, 0.4989891052246094, 0.532893717288971, 0.4972163438796997, 0.5359013080596924, 0.4705846309661865, 0.4304530620574951, 0.4824105501174927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0153167247772217})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5122703909873962})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38390612602233887})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3760688602924347})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3481910824775696})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3460826277732849})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37937822937965393})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3858864903450012})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35053175687789917})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9597, 'crossentropy': 0.3149567138671875}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8491807579994202})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.49828001856803894})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.394717812538147})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32384032011032104})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.340800940990448})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3103829622268677})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30707848072052})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29201894998550415})
store['active_learning_steps'][43]['eval_training']['best_epoch']=8
store['active_learning_steps'][43]['acquisition']={'indices': [15043, 33505, 46132, 56043, 10608, 30109, 42931, 8771, 26568, 44805], 'labels': [-1, 2, 7, -1, -1, 7, 3, 3, -1, -1], 'scores': [0.3188045024871826, 0.4290205240249634, 0.605711042881012, 0.4337056279182434, 0.24383234977722168, 0.5849154591560364, 0.6108555793762207, 0.4370771646499634, 0.3741239905357361, 0.3120075464248657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0324567556381226})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5221635103225708})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36796340346336365})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35733962059020996})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3468518853187561})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32252585887908936})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3298971951007843})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.358575701713562})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3445698618888855})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.29369755859375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7864008545875549})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5282127261161804})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36715632677078247})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3365105390548706})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30780935287475586})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2880151569843292})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27553755044937134})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2829434871673584})
store['active_learning_steps'][44]['eval_training']['best_epoch']=7
store['active_learning_steps'][44]['acquisition']={'indices': [45446, 40732, 53728, 35694, 50459, 2323, 15186, 43745, 45003, 29511], 'labels': [7, -1, -1, 9, 8, -1, -1, 8, 5, -1], 'scores': [0.448238730430603, 0.5183796882629395, 0.40293264389038086, 0.47599995136260986, 0.4255955219268799, 0.3626614809036255, 0.34659385681152344, 0.4222792983055115, 0.3482397794723511, 0.4591928720474243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0855121612548828})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4821103513240814})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3808783292770386})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3383207321166992})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3045281767845154})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3100024461746216})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37020301818847656})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3459458351135254})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9621, 'crossentropy': 0.291746484375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8466812372207642})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.536597490310669})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40509605407714844})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3745432198047638})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3107573390007019})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3319641351699829})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30042946338653564})
store['active_learning_steps'][45]['eval_training']['best_epoch']=7
store['active_learning_steps'][45]['acquisition']={'indices': [24680, 24325, 31157, 42950, 41738, 29002, 32445, 30334, 935, 52205], 'labels': [-1, -1, 3, -1, 9, 7, 5, 9, 8, -1], 'scores': [0.5580763816833496, 0.5210522413253784, 0.3859151005744934, 0.3175184726715088, 0.40891021490097046, 0.4300042986869812, 0.45652487874031067, 0.4000427722930908, 0.535946786403656, 0.4176582098007202]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1685296297073364})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4753415882587433})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34147921204566956})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38557225465774536})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35812908411026})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35185110569000244})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9592, 'crossentropy': 0.338406103515625}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7510370016098022})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.502890944480896})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.44906824827194214})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4435453414916992})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3785773515701294})
store['active_learning_steps'][46]['eval_training']['best_epoch']=5
store['active_learning_steps'][46]['acquisition']={'indices': [34406, 55189, 42839, 52173, 1646, 43887, 25062, 48038, 28536, 7833], 'labels': [4, -1, 2, 7, -1, -1, -1, 3, 3, 5], 'scores': [0.4246864318847656, 0.476141095161438, 0.312583327293396, 0.4104353189468384, 0.45494091510772705, 0.3360852003097534, 0.5543415546417236, 0.4335830807685852, 0.5275717973709106, 0.4872697591781616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0072225332260132})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5081748366355896})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36677855253219604})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3405809998512268})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36070165038108826})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3664722442626953})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.351570188999176})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9593, 'crossentropy': 0.32883916015625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8065744638442993})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5340229272842407})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4284306764602661})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3797999918460846})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3454376459121704})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3523854613304138})
store['active_learning_steps'][47]['eval_training']['best_epoch']=5
store['active_learning_steps'][47]['acquisition']={'indices': [51530, 854, 43427, 5740, 24740, 52886, 15855, 40022, 45509, 45012], 'labels': [2, 2, 7, 9, 8, 7, 5, 8, 3, 5], 'scores': [0.40747058391571045, 0.4405776858329773, 0.4116409420967102, 0.49019598960876465, 0.5832110643386841, 0.4124366044998169, 0.5800038576126099, 0.30951225757598877, 0.2755594253540039, 0.4941720962524414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1027300357818604})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4846138656139374})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3909066915512085})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3625817596912384})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3192841410636902})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3639894127845764})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30491071939468384})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30805715918540955})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3296234607696533})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33165138959884644})
store['active_learning_steps'][48]['training']['best_epoch']=7
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9651, 'crossentropy': 0.2910630126953125}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8692160844802856})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5015767216682434})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4034062922000885})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3450008034706116})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3037099838256836})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28326794505119324})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2983030676841736})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29313522577285767})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28203651309013367})
store['active_learning_steps'][48]['eval_training']['best_epoch']=9
store['active_learning_steps'][48]['acquisition']={'indices': [47132, 13608, 47383, 51002, 24790, 57507, 48616, 57718, 48899, 36704], 'labels': [2, 8, 6, -1, -1, 0, -1, 7, 2, 2], 'scores': [0.44371145963668823, 0.49428024888038635, 0.4288194179534912, 0.3731313943862915, 0.40807461738586426, 0.5586209893226624, 0.5119214057922363, 0.5738722085952759, 0.3568991422653198, 0.6860371232032776]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.2347354888916016})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49472343921661377})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35457295179367065})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3357774615287781})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3372831344604492})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.311792254447937})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3136754631996155})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26739999651908875})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3147844672203064})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2985144853591919})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31175529956817627})
store['active_learning_steps'][49]['training']['best_epoch']=8
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.277687353515625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.860465407371521})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4936133623123169})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36565130949020386})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.364040732383728})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3001260757446289})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26718759536743164})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28404563665390015})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26552873849868774})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26131170988082886})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2365449070930481})
store['active_learning_steps'][49]['eval_training']['best_epoch']=10
store['active_learning_steps'][49]['acquisition']={'indices': [39162, 26760, 37503, 11195, 10151, 29621, 53991, 44350, 29620, 43307], 'labels': [-1, 8, -1, -1, 8, -1, -1, 3, -1, -1], 'scores': [0.5324913859367371, 0.4550095796585083, 0.4940606355667114, 0.6796014904975891, 0.49306392669677734, 0.527546226978302, 0.5634297132492065, 0.49457138776779175, 0.5524528622627258, 0.5572911500930786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0967228412628174})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5178794860839844})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4523993134498596})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.378130704164505})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3024054765701294})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3192770481109619})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29823577404022217})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32330015301704407})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30298322439193726})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34892508387565613})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.2744755126953125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9737861156463623})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5683457851409912})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41612276434898376})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3910161852836609})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3068111538887024})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2972620725631714})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3235930800437927})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29668575525283813})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2887670397758484})
store['active_learning_steps'][50]['eval_training']['best_epoch']=9
store['active_learning_steps'][50]['acquisition']={'indices': [46822, 2152, 48618, 29828, 34414, 45602, 3932, 15832, 3218, 30159], 'labels': [-1, -1, 9, -1, 8, 5, -1, -1, 4, 3], 'scores': [0.2983741760253906, 0.4457281827926636, 0.33047300577163696, 0.5261562466621399, 0.5178358554840088, 0.6785635352134705, 0.6306825876235962, 0.33419233560562134, 0.32551151514053345, 0.5139923095703125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1464173793792725})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5521842837333679})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36622631549835205})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3707091808319092})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34577563405036926})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30739879608154297})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.361452579498291})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3171468675136566})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3148680627346039})
store['active_learning_steps'][51]['training']['best_epoch']=6
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.281569677734375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9138345718383789})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4718090295791626})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3989298641681671})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3436208963394165})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3064582645893097})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2881377935409546})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28896084427833557})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2717946767807007})
store['active_learning_steps'][51]['eval_training']['best_epoch']=8
store['active_learning_steps'][51]['acquisition']={'indices': [39162, 49545, 20897, 9417, 28352, 18027, 15744, 17947, 33953, 6044], 'labels': [-1, 8, -1, 6, -1, -1, -1, -1, -1, 2], 'scores': [0.4377298355102539, 0.460806667804718, 0.3347576856613159, 0.48123204708099365, 0.3508804440498352, 0.2699902057647705, 0.4201406240463257, 0.4113650321960449, 0.32589244842529297, 0.5012034773826599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.132541537284851})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5485114455223083})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4394361078739166})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35640496015548706})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3659015893936157})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3211958408355713})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3323732614517212})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33654195070266724})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32519468665122986})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.2824279541015625}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8223398923873901})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5019550323486328})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4231691360473633})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3832625150680542})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3524126410484314})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.35746055841445923})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29276999831199646})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3102310597896576})
store['active_learning_steps'][52]['eval_training']['best_epoch']=7
store['active_learning_steps'][52]['acquisition']={'indices': [763, 51987, 33812, 48103, 53790, 56086, 18864, 48512, 13093, 40644], 'labels': [-1, 3, 6, 4, -1, -1, -1, 5, 3, 1], 'scores': [0.6669650077819824, 0.3530558943748474, 0.6330632567405701, 0.3054509162902832, 0.35414230823516846, 0.5121304988861084, 0.5647215247154236, 0.37414640188217163, 0.6522496938705444, 0.4993210434913635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.136849284172058})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5424792766571045})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41045260429382324})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37748652696609497})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.333878755569458})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32082629203796387})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3076334297657013})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3263383209705353})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3190254271030426})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32543742656707764})
store['active_learning_steps'][53]['training']['best_epoch']=7
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2855126953125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8754786252975464})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5030503869056702})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4034014642238617})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34577614068984985})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27140098810195923})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28610268235206604})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29136979579925537})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2794138789176941})
store['active_learning_steps'][53]['eval_training']['best_epoch']=5
store['active_learning_steps'][53]['acquisition']={'indices': [10089, 34700, 48382, 29845, 43248, 24078, 44538, 25404, 50895, 47762], 'labels': [6, -1, 8, -1, 9, 0, -1, -1, -1, 9], 'scores': [0.3621654510498047, 0.317862868309021, 0.37576955556869507, 0.3227043151855469, 0.3858456015586853, 0.5250859260559082, 0.474501371383667, 0.4500126838684082, 0.4644008278846741, 0.36766451597213745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.2826755046844482})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5884775519371033})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4180123209953308})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3484911620616913})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3685494065284729})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2942050099372864})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33126330375671387})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2933783531188965})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3133692443370819})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3007797598838806})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30380845069885254})
store['active_learning_steps'][54]['training']['best_epoch']=8
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.2499617431640625}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.857300877571106})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48522841930389404})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3541659712791443})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2876345217227936})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28603240847587585})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23678439855575562})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27429625391960144})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25900086760520935})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2510438561439514})
store['active_learning_steps'][54]['eval_training']['best_epoch']=6
store['active_learning_steps'][54]['acquisition']={'indices': [44622, 45619, 33598, 11889, 51146, 35168, 11588, 22253, 1035, 58676], 'labels': [-1, 3, -1, 5, -1, -1, -1, -1, 3, -1], 'scores': [0.3121602535247803, 0.5090310573577881, 0.40857183933258057, 0.4228743612766266, 0.4731072187423706, 0.43094563484191895, 0.5000081062316895, 0.31925272941589355, 0.546256422996521, 0.32053840160369873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0275087356567383})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.49439921975135803})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3655431270599365})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30872225761413574})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27609983086586})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.275627464056015})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28975197672843933})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2734156548976898})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26837146282196045})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30076220631599426})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2953417897224426})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3156111240386963})
store['active_learning_steps'][55]['training']['best_epoch']=9
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.26292412109375}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8225464820861816})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5033175945281982})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3517604172229767})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35267531871795654})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2997881770133972})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2943492531776428})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25183790922164917})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2532039284706116})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2542738914489746})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2589108943939209})
store['active_learning_steps'][55]['eval_training']['best_epoch']=7
store['active_learning_steps'][55]['acquisition']={'indices': [49889, 33443, 12835, 5933, 22578, 42933, 54432, 47405, 28356, 19362], 'labels': [0, -1, -1, -1, -1, 4, 2, -1, -1, 8], 'scores': [0.5596767067909241, 0.33904099464416504, 0.5389539003372192, 0.2816197872161865, 0.38159334659576416, 0.3296887278556824, 0.36233794689178467, 0.44306695461273193, 0.22649896144866943, 0.5421534776687622]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.2609095573425293})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6167317628860474})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.409681499004364})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37245190143585205})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3863885998725891})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32625719904899597})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31415775418281555})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3145008087158203})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3430720269680023})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33766114711761475})
store['active_learning_steps'][56]['training']['best_epoch']=7
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2783479248046875}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9141777753829956})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49607053399086})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4245494604110718})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34477800130844116})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3639509081840515})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3029204308986664})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32919999957084656})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3007810115814209})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29487136006355286})
store['active_learning_steps'][56]['eval_training']['best_epoch']=9
store['active_learning_steps'][56]['acquisition']={'indices': [29109, 39595, 40939, 53357, 17545, 51130, 49164, 3290, 43606, 26642], 'labels': [-1, -1, -1, -1, -1, -1, -1, 4, -1, 7], 'scores': [0.5924493074417114, 0.4754072427749634, 0.5500190854072571, 0.7059703469276428, 0.43925249576568604, 0.623424768447876, 0.7302524447441101, 0.46086347103118896, 0.8369341492652893, 0.5039738416671753]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.3286924362182617})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5523784160614014})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3537321090698242})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3163074254989624})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29478102922439575})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3102285861968994})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25063133239746094})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27768829464912415})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2891811430454254})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28019070625305176})
store['active_learning_steps'][57]['training']['best_epoch']=7
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2494195068359375}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.786237359046936})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4680083394050598})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3395017981529236})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33347511291503906})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3156580328941345})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31542056798934937})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29912447929382324})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27776384353637695})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2607019543647766})
store['active_learning_steps'][57]['eval_training']['best_epoch']=9
store['active_learning_steps'][57]['acquisition']={'indices': [48305, 32447, 28136, 23086, 52383, 50960, 14487, 1075, 49801, 17941], 'labels': [-1, -1, 8, 8, -1, -1, -1, 7, -1, 0], 'scores': [0.4192432165145874, 0.38933026790618896, 0.36708664894104004, 0.45312023162841797, 0.467434287071228, 0.5665764808654785, 0.33797454833984375, 0.6956725120544434, 0.43570876121520996, 0.5006058812141418]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0492782592773438})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.545828104019165})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4072006940841675})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3556596338748932})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3250234127044678})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33379578590393066})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31355494260787964})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29324108362197876})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3047856390476227})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27854782342910767})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3201298117637634})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29647400975227356})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37208887934684753})
store['active_learning_steps'][58]['training']['best_epoch']=10
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.2683188720703125}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8311983346939087})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.47652316093444824})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34719139337539673})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32069966197013855})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29016008973121643})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2767302393913269})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24303928017616272})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24355077743530273})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2422063946723938})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2262781858444214})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2436220347881317})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25246208906173706})
store['active_learning_steps'][58]['eval_training']['best_epoch']=10
store['active_learning_steps'][58]['acquisition']={'indices': [5440, 4153, 49589, 52926, 44840, 22939, 45529, 57677, 11145, 12497], 'labels': [-1, 2, 3, -1, -1, -1, 8, -1, -1, 0], 'scores': [0.46626877784729004, 0.4402509331703186, 0.47676169872283936, 0.5427702069282532, 0.39245617389678955, 0.4635612964630127, 0.51568603515625, 0.5079160332679749, 0.593501627445221, 0.5401605665683746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2700910568237305})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6116676330566406})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3994686007499695})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.331159770488739})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33975648880004883})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31567955017089844})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3188663125038147})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27748578786849976})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3032958507537842})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3125963807106018})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3096138536930084})
store['active_learning_steps'][59]['training']['best_epoch']=8
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.26002783203125}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.831735372543335})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5117287039756775})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41159629821777344})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34443730115890503})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31015193462371826})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2892075777053833})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29140597581863403})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2969051003456116})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25591444969177246})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3051949143409729})
store['active_learning_steps'][59]['eval_training']['best_epoch']=9
store['active_learning_steps'][59]['acquisition']={'indices': [6117, 6813, 37048, 14171, 49985, 52800, 29168, 15743, 34133, 5138], 'labels': [-1, -1, 9, -1, 3, 9, -1, 3, -1, -1], 'scores': [0.5350954532623291, 0.36050450801849365, 0.42237013578414917, 0.5897688269615173, 0.4807294011116028, 0.6161708235740662, 0.4860454797744751, 0.457065224647522, 0.376112163066864, 0.34264373779296875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1685755252838135})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5164580345153809})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.40663811564445496})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3515087366104126})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31507694721221924})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3121334910392761})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31299418210983276})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28516557812690735})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2860074043273926})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3203694820404053})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.30115044116973877})
store['active_learning_steps'][60]['training']['best_epoch']=8
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.27247265625}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0029988288879395})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5326424837112427})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44149792194366455})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3299400806427002})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3279111385345459})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2860535979270935})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2867809534072876})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2990918755531311})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2612808346748352})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25000476837158203})
store['active_learning_steps'][60]['eval_training']['best_epoch']=10
store['active_learning_steps'][60]['acquisition']={'indices': [11357, 37256, 31562, 49117, 1925, 13942, 5244, 42508, 54820, 30764], 'labels': [-1, 6, 3, 3, -1, 4, -1, 3, -1, 7], 'scores': [0.4135550260543823, 0.4740453362464905, 0.4784938395023346, 0.46397536993026733, 0.3764117956161499, 0.526343822479248, 0.35298430919647217, 0.4922538995742798, 0.30213892459869385, 0.49756985902786255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0994281768798828})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5260206460952759})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4238913655281067})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33900365233421326})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28625041246414185})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2833525538444519})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2949522137641907})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26128044724464417})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28410694003105164})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.28452208638191223})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3074150085449219})
store['active_learning_steps'][61]['training']['best_epoch']=8
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.262453125}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9865415096282959})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5110406875610352})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4019950032234192})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3496815860271454})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28580406308174133})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25912225246429443})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23394879698753357})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26875391602516174})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24536022543907166})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24227148294448853})
store['active_learning_steps'][61]['eval_training']['best_epoch']=7
store['active_learning_steps'][61]['acquisition']={'indices': [30388, 11282, 15289, 41799, 9173, 8204, 2232, 39146, 56086, 10669], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4523797631263733, 0.49519139528274536, 0.31522101163864136, 0.4443640112876892, 0.37307560443878174, 0.49611926078796387, 0.3673436641693115, 0.49287426471710205, 0.42177772521972656, 0.30561041831970215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1215012073516846})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.5684323310852051})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3723965883255005})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.310990571975708})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2751055955886841})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2734094262123108})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.22226831316947937})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25715184211730957})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2560204565525055})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.22335250675678253})
store['active_learning_steps'][62]['training']['best_epoch']=7
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9748, 'crossentropy': 0.2277670166015625}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8735958337783813})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5683943629264832})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3835763931274414})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37404951453208923})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.318495512008667})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3175138831138611})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2484895884990692})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24693343043327332})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.26286768913269043})
store['active_learning_steps'][62]['eval_training']['best_epoch']=8
store['active_learning_steps'][62]['acquisition']={'indices': [42586, 50343, 11706, 32402, 7126, 39609, 41362, 56086, 24449, 1955], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3053903579711914, 0.35833799839019775, 0.547349214553833, 0.6745936870574951, 0.4444093108177185, 0.5543454885482788, 0.4517132043838501, 0.6352845430374146, 0.3605860471725464, 0.4367259740829468]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.148724913597107})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6830644607543945})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45284581184387207})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3220682740211487})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3023393154144287})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29770147800445557})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26970574259757996})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27980273962020874})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2618812322616577})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30210140347480774})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30268973112106323})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2781388759613037})
store['active_learning_steps'][63]['training']['best_epoch']=9
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.2679650634765625}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9180169105529785})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5071866512298584})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39853930473327637})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3699517846107483})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.28330954909324646})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.287341833114624})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2845887839794159})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24700914323329926})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2565953731536865})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2264764904975891})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24742457270622253})
store['active_learning_steps'][63]['eval_training']['best_epoch']=10
store['active_learning_steps'][63]['acquisition']={'indices': [18277, 39222, 21466, 11711, 46324, 37138, 40902, 47321, 24760, 51834], 'labels': [-1, -1, -1, 2, -1, -1, -1, 2, -1, -1], 'scores': [0.45255422592163086, 0.4146062135696411, 0.47291797399520874, 0.6424010694026947, 0.3781602382659912, 0.35293495655059814, 0.4074636697769165, 0.4650680422782898, 0.41531383991241455, 0.4876245856285095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.186535358428955})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5814713835716248})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3877773880958557})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37523919343948364})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2924407124519348})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30110397934913635})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27536335587501526})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2672327160835266})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2874155044555664})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26592719554901123})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2598832845687866})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3010769188404083})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2794100344181061})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31204965710639954})
store['active_learning_steps'][64]['training']['best_epoch']=11
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.2560207763671875}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9167994260787964})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46555012464523315})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32338809967041016})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31110310554504395})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24936053156852722})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2813052535057068})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2757412791252136})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23704902827739716})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27359288930892944})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.21737289428710938})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22597378492355347})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.22661124169826508})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22922739386558533})
store['active_learning_steps'][64]['eval_training']['best_epoch']=10
store['active_learning_steps'][64]['acquisition']={'indices': [33799, 35235, 25813, 2659, 43394, 27943, 18975, 47621, 19791, 4751], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4990067481994629, 0.5289274454116821, 0.2689468264579773, 0.4906100034713745, 0.5097478628158569, 0.48493921756744385, 0.4227514863014221, 0.5240709781646729, 0.7220628261566162, 0.4542776346206665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2341073751449585})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6149389147758484})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4348451495170593})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38502150774002075})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3460109233856201})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32916414737701416})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29163169860839844})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3217611014842987})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3273078203201294})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31951385736465454})
store['active_learning_steps'][65]['training']['best_epoch']=7
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.288014794921875}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8587943911552429})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4776841998100281})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35998842120170593})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3259238004684448})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3140996992588043})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30641141533851624})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2759122848510742})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28124934434890747})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2632772624492645})
store['active_learning_steps'][65]['eval_training']['best_epoch']=9
store['active_learning_steps'][65]['acquisition']={'indices': [134, 1148, 2765, 52914, 7911, 38242, 3810, 22704, 19673, 25551], 'labels': [1, 1, 0, 5, -1, 7, -1, 5, -1, -1], 'scores': [0.5479722619056702, 0.4887775182723999, 0.5981508493423462, 0.43942129611968994, 0.3745938539505005, 0.5430809259414673, 0.36719775199890137, 0.4831373691558838, 0.36564987897872925, 0.41566064953804016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.383508563041687})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.67790687084198})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3871943950653076})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38615328073501587})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35024112462997437})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3024105131626129})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2984096109867096})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28926095366477966})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2972632646560669})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3178017735481262})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3156867027282715})
store['active_learning_steps'][66]['training']['best_epoch']=8
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.291046337890625}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9621400833129883})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5501981377601624})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4011715054512024})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37465614080429077})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3374614715576172})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31094807386398315})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3405270576477051})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3193967342376709})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31624770164489746})
store['active_learning_steps'][66]['eval_training']['best_epoch']=6
store['active_learning_steps'][66]['acquisition']={'indices': [32573, 25036, 20150, 1512, 11598, 53336, 21396, 58812, 49672, 19937], 'labels': [8, -1, 3, 0, 4, -1, -1, 3, -1, -1], 'scores': [0.50681471824646, 0.38300609588623047, 0.5461903810501099, 0.6119980812072754, 0.43676161766052246, 0.3908853530883789, 0.3563727140426636, 0.48820960521698, 0.5020080804824829, 0.31785154342651367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.1405601501464844})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5959317684173584})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3900735378265381})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3202882409095764})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2917410135269165})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2795085608959198})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2797926068305969})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31841373443603516})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27760744094848633})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29768460988998413})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2860683798789978})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32989412546157837})
store['active_learning_steps'][67]['training']['best_epoch']=9
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.276931396484375}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9056059122085571})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4618915915489197})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37742215394973755})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29593920707702637})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.314438134431839})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2994520664215088})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2512490153312683})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25350892543792725})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25411441922187805})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27181750535964966})
store['active_learning_steps'][67]['eval_training']['best_epoch']=7
store['active_learning_steps'][67]['acquisition']={'indices': [53978, 5801, 35065, 32697, 17760, 39846, 9063, 8202, 25231, 47676], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, -1, -1], 'scores': [0.41550254821777344, 0.4689018726348877, 0.40813517570495605, 0.4319347143173218, 0.37634027004241943, 0.5156741142272949, 0.43787074089050293, 0.34535861015319824, 0.528922438621521, 0.42315590381622314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.2830191850662231})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5371698141098022})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39214441180229187})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34424513578414917})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3350510597229004})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2703579068183899})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2910608649253845})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26367712020874023})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2525862753391266})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28771907091140747})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.253176748752594})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2911378741264343})
store['active_learning_steps'][68]['training']['best_epoch']=9
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.2643901611328125}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0448002815246582})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5208936929702759})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.40566402673721313})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3619728088378906})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3617349863052368})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3016546368598938})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2633407413959503})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2834125757217407})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2719240188598633})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25439924001693726})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23269429802894592})
store['active_learning_steps'][68]['eval_training']['best_epoch']=11
store['active_learning_steps'][68]['acquisition']={'indices': [55629, 56432, 48497, 10220, 29611, 31231, 49989, 48735, 36668, 32429], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5675927996635437, 0.3187028169631958, 0.5017573833465576, 0.49796974658966064, 0.5974466800689697, 0.45874112844467163, 0.6021841764450073, 0.6795966029167175, 0.4693284034729004, 0.4664119482040405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.3936184644699097})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6615315675735474})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.4698084890842438})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34884458780288696})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31898730993270874})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28155872225761414})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2768356204032898})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3017314076423645})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32299527525901794})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28984928131103516})
store['active_learning_steps'][69]['training']['best_epoch']=7
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.300045166015625}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.916214108467102})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4823261499404907})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.45036953687667847})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33087748289108276})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33547279238700867})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31901437044143677})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3260713219642639})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3170008063316345})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25842514634132385})
store['active_learning_steps'][69]['eval_training']['best_epoch']=9
store['active_learning_steps'][69]['acquisition']={'indices': [38275, 49164, 21576, 52981, 59460, 16208, 35248, 43897, 28512, 22507], 'labels': [2, -1, 0, 5, 1, 3, 3, 1, 5, 8], 'scores': [0.444405734539032, 0.30346131324768066, 0.32692813873291016, 0.5785799622535706, 0.4112672805786133, 0.20426654815673828, 0.3625977039337158, 0.4866740107536316, 0.5705433487892151, 0.2858976125717163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1364487409591675})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5294232368469238})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35049569606781006})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31655439734458923})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27105197310447693})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2432413399219513})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2424677312374115})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23597075045108795})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25036126375198364})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2534743845462799})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2731030583381653})
store['active_learning_steps'][70]['training']['best_epoch']=8
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.2455996337890625}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9931105971336365})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5418179631233215})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4221460223197937})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3129899501800537})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27670684456825256})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25894293189048767})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25689005851745605})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25014767050743103})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22436608374118805})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2366192638874054})
store['active_learning_steps'][70]['eval_training']['best_epoch']=9
store['active_learning_steps'][70]['acquisition']={'indices': [11622, 33770, 29037, 55368, 32880, 47784, 28905, 7673, 253, 57802], 'labels': [-1, -1, -1, 8, 0, -1, -1, -1, -1, -1], 'scores': [0.45721960067749023, 0.45936334133148193, 0.5131793022155762, 0.48855704069137573, 0.6606969237327576, 0.41218507289886475, 0.3993571996688843, 0.4607936143875122, 0.47728776931762695, 0.41300225257873535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.331925630569458})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6059169769287109})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4407550096511841})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.34886282682418823})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33003586530685425})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30475378036499023})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28853076696395874})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28796327114105225})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3015827238559723})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.308682382106781})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.27544474601745605})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27142003178596497})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27786943316459656})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.312397301197052})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2962026596069336})
store['active_learning_steps'][71]['training']['best_epoch']=12
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9739, 'crossentropy': 0.263309716796875}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 1.0604004859924316})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.522415041923523})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38221055269241333})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.314319372177124})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2998068928718567})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.26103127002716064})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2826845943927765})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.263159841299057})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2447863221168518})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23506221175193787})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2390279918909073})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25743401050567627})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23088964819908142})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2124078869819641})
store['active_learning_steps'][71]['eval_training']['best_epoch']=14
store['active_learning_steps'][71]['acquisition']={'indices': [5000, 9067, 51019, 49890, 12054, 6316, 8543, 22072, 11685, 14384], 'labels': [7, -1, -1, 5, -1, -1, -1, -1, -1, -1], 'scores': [0.4137447774410248, 0.5571501851081848, 0.32386183738708496, 0.6120424866676331, 0.3886559009552002, 0.26685619354248047, 0.4118920564651489, 0.22778236865997314, 0.3086585998535156, 0.5804958343505859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2245105504989624})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6613856554031372})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3977091610431671})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31978917121887207})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2684738337993622})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2926088571548462})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2561084032058716})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25309914350509644})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26515161991119385})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.264078289270401})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26102614402770996})
store['active_learning_steps'][72]['training']['best_epoch']=8
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.2501526611328125}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9177120923995972})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.49707579612731934})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4224517345428467})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30854734778404236})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2947922348976135})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27920037508010864})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2938328981399536})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25808054208755493})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25028330087661743})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2340054214000702})
store['active_learning_steps'][72]['eval_training']['best_epoch']=10
store['active_learning_steps'][72]['acquisition']={'indices': [28190, 34020, 45806, 2031, 41840, 21211, 13414, 59731, 12186, 53058], 'labels': [4, -1, 7, -1, -1, -1, -1, 5, -1, -1], 'scores': [0.30196231603622437, 0.30716264247894287, 0.4855620265007019, 0.5610088109970093, 0.5196213722229004, 0.7097189426422119, 0.5282726287841797, 0.703827977180481, 0.4727550745010376, 0.3744097948074341]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0811200141906738})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5303740501403809})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4026506543159485})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3093053102493286})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27495306730270386})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26521092653274536})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2802847623825073})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26245152950286865})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2568913698196411})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2765263617038727})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25569093227386475})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2933879494667053})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26138338446617126})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30882149934768677})
store['active_learning_steps'][73]['training']['best_epoch']=11
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.2623298828125}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8735235929489136})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5020003318786621})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40423691272735596})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35497188568115234})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2748854160308838})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2694580554962158})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26517388224601746})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2589815557003021})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2343338429927826})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23679029941558838})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29127782583236694})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2449658066034317})
store['active_learning_steps'][73]['eval_training']['best_epoch']=9
store['active_learning_steps'][73]['acquisition']={'indices': [49316, 40549, 39301, 30121, 5341, 16690, 53560, 46677, 31114, 23087], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 4, -1], 'scores': [0.2754974365234375, 0.5429731011390686, 0.3553476333618164, 0.3061438798904419, 0.4024026393890381, 0.4435315728187561, 0.4579390287399292, 0.32048118114471436, 0.5825334787368774, 0.4434998035430908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.324101209640503})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6230134963989258})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.38645845651626587})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3313620686531067})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3231448233127594})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2899005711078644})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3055301904678345})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2718064486980438})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2666066884994507})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2516366243362427})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2752595543861389})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.258407324552536})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27211400866508484})
store['active_learning_steps'][74]['training']['best_epoch']=10
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9742, 'crossentropy': 0.251615869140625}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0638413429260254})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5551039576530457})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3757610321044922})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29609906673431396})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28341609239578247})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.292477548122406})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25618356466293335})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2754261791706085})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2722633481025696})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2555553913116455})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23860536515712738})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2313346266746521})
store['active_learning_steps'][74]['eval_training']['best_epoch']=12
store['active_learning_steps'][74]['acquisition']={'indices': [53073, 54880, 7352, 35693, 10717, 49517, 50520, 52379, 58297, 21549], 'labels': [-1, 5, -1, -1, -1, 6, -1, -1, -1, -1], 'scores': [0.44187361001968384, 0.4254501461982727, 0.5701532363891602, 0.5776565670967102, 0.3362615704536438, 0.6702110171318054, 0.5660980939865112, 0.4265460968017578, 0.5852718353271484, 0.5850255489349365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.2027078866958618})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5928477048873901})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.4404904246330261})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3249117136001587})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3494529724121094})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2791632413864136})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28504425287246704})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.308651864528656})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2798691987991333})
store['active_learning_steps'][75]['training']['best_epoch']=6
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.29216611328125}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0046074390411377})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5811776518821716})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42240577936172485})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3574017882347107})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3313028812408447})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34634196758270264})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33322566747665405})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32691437005996704})
store['active_learning_steps'][75]['eval_training']['best_epoch']=8
store['active_learning_steps'][75]['acquisition']={'indices': [56253, 53979, 39411, 35688, 47207, 46344, 25630, 25534, 34913, 46998], 'labels': [-1, 8, 2, 3, -1, -1, -1, -1, -1, -1], 'scores': [0.4276237487792969, 0.48184412717819214, 0.6204162240028381, 0.331950306892395, 0.48450595140457153, 0.31715697050094604, 0.3898921012878418, 0.4601519703865051, 0.44019901752471924, 0.3787180185317993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.2352209091186523})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5767977833747864})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.46358978748321533})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39140844345092773})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3646303117275238})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2670333981513977})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30555304884910583})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2855278253555298})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26980990171432495})
store['active_learning_steps'][76]['training']['best_epoch']=6
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.2785809326171875}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8635433912277222})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49304860830307007})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4173646569252014})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38563334941864014})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30563873052597046})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.325761616230011})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33156222105026245})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29061388969421387})
store['active_learning_steps'][76]['eval_training']['best_epoch']=8
store['active_learning_steps'][76]['acquisition']={'indices': [56658, 43952, 7596, 9098, 54978, 46148, 30344, 44284, 17486, 5079], 'labels': [-1, -1, 4, 2, -1, 9, -1, -1, 7, -1], 'scores': [0.4485870599746704, 0.48042309284210205, 0.5125250816345215, 0.42846179008483887, 0.2934103012084961, 0.41140466928482056, 0.2816556692123413, 0.34148526191711426, 0.4974462389945984, 0.352419912815094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.145323395729065})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5792937874794006})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.43014079332351685})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.37402790784835815})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32054609060287476})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28592973947525024})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2957937717437744})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2520686984062195})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2939850091934204})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30577975511550903})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3129242956638336})
store['active_learning_steps'][77]['training']['best_epoch']=8
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.256929833984375}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.9221862554550171})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5190531015396118})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3902450203895569})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3061859905719757})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30049318075180054})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28723230957984924})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2769406735897064})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27502840757369995})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23383241891860962})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26375171542167664})
store['active_learning_steps'][77]['eval_training']['best_epoch']=9
store['active_learning_steps'][77]['acquisition']={'indices': [52973, 648, 48103, 14757, 3773, 1109, 23113, 37184, 26186, 9687], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 6, 0], 'scores': [0.37490105628967285, 0.2755016088485718, 0.4032197594642639, 0.46403419971466064, 0.42500436305999756, 0.26426243782043457, 0.3562973737716675, 0.4394685626029968, 0.3752620220184326, 0.47133970260620117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.3214579820632935})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5962127447128296})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3734866976737976})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3702651262283325})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3183255195617676})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27750328183174133})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24476955831050873})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2679898738861084})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27993518114089966})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2649407982826233})
store['active_learning_steps'][78]['training']['best_epoch']=7
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.285150927734375}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8318268656730652})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5381031036376953})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39593809843063354})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36086124181747437})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3100655674934387})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2873392403125763})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27480852603912354})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2754887640476227})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2580227553844452})
store['active_learning_steps'][78]['eval_training']['best_epoch']=9
store['active_learning_steps'][78]['acquisition']={'indices': [48307, 6818, 49634, 24587, 36331, 18724, 52910, 31738, 53568, 31509], 'labels': [-1, 7, 8, 8, -1, -1, 9, 8, 5, -1], 'scores': [0.1444072723388672, 0.3580930233001709, 0.38578569889068604, 0.30725300312042236, 0.4178236722946167, 0.4110339879989624, 0.5159551501274109, 0.5874174237251282, 0.4700092673301697, 0.3588752746582031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.357265591621399})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.6122565269470215})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3532370924949646})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3185946047306061})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3189593255519867})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27141401171684265})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28033924102783203})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27219244837760925})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2620459794998169})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25307750701904297})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2745670676231384})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26253268122673035})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2730080485343933})
store['active_learning_steps'][79]['training']['best_epoch']=10
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.270099267578125}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.918326735496521})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5145521759986877})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.365838885307312})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.313487708568573})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2978704571723938})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.290611207485199})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2797875702381134})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2562822103500366})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2732662558555603})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28958266973495483})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2506195604801178})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25389134883880615})
store['active_learning_steps'][79]['eval_training']['best_epoch']=11
store['active_learning_steps'][79]['acquisition']={'indices': [5261, 40593, 21173, 14130, 30965, 47405, 24861, 45486, 3836, 51722], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 4], 'scores': [0.5017303228378296, 0.4022698402404785, 0.4441283941268921, 0.498818039894104, 0.43247246742248535, 0.4596853256225586, 0.47889065742492676, 0.4458353519439697, 0.4739574193954468, 0.480175256729126]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.314507007598877})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.6475491523742676})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4122985601425171})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33516737818717957})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2835790514945984})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2922170162200928})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2562335729598999})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25987306237220764})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25830507278442383})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2618556618690491})
store['active_learning_steps'][80]['training']['best_epoch']=7
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9739, 'crossentropy': 0.2406787841796875}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9553467035293579})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5408828258514404})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37613624334335327})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3163033425807953})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29124927520751953})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28544777631759644})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2416798621416092})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2666710615158081})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.263820618391037})
store['active_learning_steps'][80]['eval_training']['best_epoch']=7
store['active_learning_steps'][80]['acquisition']={'indices': [14864, 12959, 935, 7688, 30242, 14691, 21377, 42428, 33583, 42973], 'labels': [3, -1, -1, -1, -1, -1, -1, 5, -1, 4], 'scores': [0.49793124198913574, 0.457025408744812, 0.4355020523071289, 0.6011280417442322, 0.28774523735046387, 0.2305617332458496, 0.4412339925765991, 0.5275443196296692, 0.4260556697845459, 0.511120617389679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.0956228971481323})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5897490978240967})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.40825700759887695})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36020034551620483})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.296675443649292})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2762605845928192})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26620805263519287})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2977338135242462})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2791587710380554})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2976624369621277})
store['active_learning_steps'][81]['training']['best_epoch']=7
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.245026171875}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9009328484535217})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.508612871170044})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37869030237197876})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.312610387802124})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29895490407943726})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27950891852378845})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2416904866695404})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2484230399131775})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2480250895023346})
store['active_learning_steps'][81]['eval_training']['best_epoch']=7
store['active_learning_steps'][81]['acquisition']={'indices': [55970, 58459, 56719, 34673, 46734, 12168, 28564, 27637, 28808, 40704], 'labels': [-1, -1, 2, -1, 4, -1, -1, -1, -1, 5], 'scores': [0.4001117944717407, 0.4008036255836487, 0.3523294925689697, 0.3702046871185303, 0.4879732131958008, 0.5249140858650208, 0.2792240381240845, 0.39265626668930054, 0.3390160799026489, 0.4915100336074829]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.1324961185455322})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5629112720489502})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4079238176345825})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36509254574775696})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3170056641101837})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2993197441101074})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29438790678977966})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2637581527233124})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28868335485458374})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2752651572227478})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28093165159225464})
store['active_learning_steps'][82]['training']['best_epoch']=8
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9723, 'crossentropy': 0.24164765625}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.930912971496582})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5426978468894958})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.42097705602645874})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30965638160705566})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32551515102386475})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3011738657951355})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2560584545135498})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.290175199508667})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.3001491129398346})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28838667273521423})
store['active_learning_steps'][82]['eval_training']['best_epoch']=7
store['active_learning_steps'][82]['acquisition']={'indices': [23210, 49975, 37663, 31658, 13675, 8229, 11829, 18253, 11345, 30292], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.47365856170654297, 0.2948077917098999, 0.5759619474411011, 0.4631515145301819, 0.23867177963256836, 0.5033604502677917, 0.4033151865005493, 0.38803160190582275, 0.44454526901245117, 0.3671025037765503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.2224915027618408})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.622562050819397})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3961169719696045})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3599734902381897})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30028438568115234})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2980731129646301})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2873680889606476})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2775174081325531})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25254756212234497})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28218942880630493})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25974148511886597})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24773991107940674})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25458693504333496})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2630611062049866})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2882368564605713})
store['active_learning_steps'][83]['training']['best_epoch']=12
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.2580243408203125}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9722123146057129})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5364325642585754})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40688860416412354})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.34520936012268066})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3262229561805725})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28268754482269287})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26856476068496704})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2373124361038208})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24687127768993378})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24898123741149902})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27343982458114624})
store['active_learning_steps'][83]['eval_training']['best_epoch']=8
store['active_learning_steps'][83]['acquisition']={'indices': [17169, 42758, 4976, 8065, 51826, 54856, 50355, 44341, 22578, 7312], 'labels': [-1, -1, -1, -1, -1, -1, 6, -1, -1, -1], 'scores': [0.34308934211730957, 0.310763955116272, 0.4911113977432251, 0.43075621128082275, 0.6298639178276062, 0.4282088279724121, 0.38775157928466797, 0.4910616874694824, 0.3689981698989868, 0.4518747329711914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1726999282836914})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5325541496276855})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38120603561401367})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3329203724861145})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2569897472858429})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2712140679359436})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.27348652482032776})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26827502250671387})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9747, 'crossentropy': 0.260231103515625}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0186681747436523})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.546747088432312})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4511831998825073})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35208195447921753})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35586899518966675})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3083232045173645})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.36271530389785767})
store['active_learning_steps'][84]['eval_training']['best_epoch']=6
store['active_learning_steps'][84]['acquisition']={'indices': [32276, 20037, 27678, 4955, 17603, 56344, 48912, 41165, 19610, 35447], 'labels': [3, 8, 8, 2, 0, -1, 2, -1, -1, -1], 'scores': [0.6852286458015442, 0.6984220743179321, 0.32545238733291626, 0.3903921842575073, 0.42844343185424805, 0.303729772567749, 0.42165863513946533, 0.29277491569519043, 0.2992474436759949, 0.24623560905456543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.208822250366211})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.583036482334137})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3984018862247467})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3047493100166321})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26555225253105164})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2583066523075104})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2863881289958954})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.257946252822876})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2437862902879715})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.251338392496109})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2600049674510956})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26029321551322937})
store['active_learning_steps'][85]['training']['best_epoch']=9
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2548906005859375}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9162334203720093})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4833495020866394})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.37348270416259766})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3148190975189209})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2983614504337311})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29888543486595154})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.273715615272522})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27110791206359863})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24660435318946838})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2222789227962494})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2640647292137146})
store['active_learning_steps'][85]['eval_training']['best_epoch']=10
store['active_learning_steps'][85]['acquisition']={'indices': [20659, 55934, 40803, 6419, 25321, 52084, 5858, 3479, 47297, 39315], 'labels': [1, -1, -1, -1, 8, -1, -1, -1, 8, -1], 'scores': [0.3893423080444336, 0.4093947410583496, 0.43431586027145386, 0.28005754947662354, 0.5819718837738037, 0.5054497718811035, 0.5224735140800476, 0.39013540744781494, 0.42786920070648193, 0.5162233114242554]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.3530945777893066})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6267455816268921})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38764244318008423})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.30341869592666626})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.36695706844329834})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2529362440109253})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2677667737007141})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2698171138763428})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.25484582781791687})
store['active_learning_steps'][86]['training']['best_epoch']=6
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.2619708984375}
