store = {}
store['timestamp']=1620923086
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=12']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=12
store['worker_id']=12
store['num_workers']=20
store['config']={'seed': 1252, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
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
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 34], ['id', 3014], ['id', 44968], ['id', 607], ['id', 24189], ['id', 9154], ['id', 29895], ['id', 26358], ['id', 41169], ['id', 39807]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9586241245269775, 0.9333850145339966, 0.7792172431945801, 0.9197906851768494, 0.9691135883331299, 0.8855127096176147, 0.8918119668960571, 0.6776351034641266, 0.8065000772476196, 0.9848848581314087]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.9030075073242188})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.8570441007614136})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.181246757507324})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.5346896648406982})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.3829517364501953})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.75, 'crossentropy': 1.7710791015625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0688302516937256})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9892364740371704})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9906127452850342})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9614073038101196})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 49094], ['id', 11709], ['id', 1178], ['id', 34341], ['id', 17045], ['id', 30121], ['id', 20230], ['id', 4758], ['id', 8317], ['id', 35326]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5836058259010315, 0.860278844833374, 0.45361101627349854, 0.6269894242286682, 0.7028581500053406, 0.755523145198822, 0.5735548734664917, 0.8088071942329407, 0.7275773286819458, 0.6870617866516113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.5958809852600098})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.7738794088363647})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.998889446258545})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.1827592849731445})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7631, 'crossentropy': 1.44207236328125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9662193655967712})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.0091006755828857})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 0.9759230017662048})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 5290], ['id', 58625], ['id', 40549], ['id', 50528], ['id', 7555], ['id', 34928], ['id', 14918], ['id', 22720], ['id', 26679], ['ood', 25282]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5405804514884949, 0.39531558752059937, 0.5993986129760742, 0.5473830699920654, 0.6290063858032227, 0.5990403890609741, 0.5858005285263062, 0.5381905436515808, 0.528518795967102, 0.4204314947128296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.2772748470306396})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.3443057537078857})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.5584478378295898})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.6287494897842407})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8058, 'crossentropy': 1.09483984375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.9059601426124573})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 0.8513959646224976})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.8512237668037415})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 8968], ['id', 39016], ['id', 17222], ['id', 49756], ['id', 2966], ['id', 32738], ['id', 36915], ['id', 8666], ['id', 11107], ['id', 43008]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5026943683624268, 0.6322718858718872, 0.37354981899261475, 0.5399916768074036, 0.405203640460968, 0.4846930503845215, 0.602887749671936, 0.5402790307998657, 0.3974616527557373, 0.487190306186676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.008695363998413})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0232454538345337})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1280993223190308})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.256028652191162})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8371, 'crossentropy': 0.912194921875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.8599652051925659})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7856366634368896})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.7692952156066895})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 21993], ['id', 20499], ['id', 59262], ['id', 19758], ['id', 59797], ['id', 17673], ['id', 54106], ['id', 22673], ['ood', 40036], ['id', 58249]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5205708146095276, 0.5689261555671692, 0.5650008320808411, 0.3534979224205017, 0.512000560760498, 0.31537187099456787, 0.6460138559341431, 0.6119676232337952, 0.3024671673774719, 0.6587088108062744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.002522349357605})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0336320400238037})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0179964303970337})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.032374620437622})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8412, 'crossentropy': 0.89413759765625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8844252228736877})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7963153123855591})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7743533849716187})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 30646], ['id', 3310], ['id', 42671], ['id', 33318], ['id', 42495], ['id', 23011], ['id', 33004], ['id', 53324], ['id', 54865], ['id', 23162]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5772160291671753, 0.31129491329193115, 0.5670899152755737, 0.4556424617767334, 0.4707416892051697, 0.4872555732727051, 0.35959869623184204, 0.5278992652893066, 0.5012600421905518, 0.3243107199668884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8306573629379272})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9573103189468384})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.893241286277771})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8814464211463928})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8733, 'crossentropy': 0.741008935546875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8844712972640991})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7192432284355164})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7244763374328613})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 41704], ['id', 19997], ['id', 26738], ['id', 8661], ['id', 44853], ['id', 15607], ['id', 38597], ['id', 41572], ['id', 41295], ['id', 4062]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3070187568664551, 0.29446470737457275, 0.36514580249786377, 0.3776131868362427, 0.32342010736465454, 0.35474371910095215, 0.44842541217803955, 0.4290297031402588, 0.42526358366012573, 0.3108344078063965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8214137554168701})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7460035085678101})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8146496415138245})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9889881014823914})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8617919683456421})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8852, 'crossentropy': 0.70165751953125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.813692569732666})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6394858360290527})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6454451680183411})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5616908073425293})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 18029], ['id', 49509], ['id', 49683], ['id', 46420], ['id', 43767], ['id', 6432], ['id', 23190], ['id', 2465], ['id', 28525], ['id', 46290]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5785725116729736, 0.5635215044021606, 0.5620757341384888, 0.4194604158401489, 0.5320619344711304, 0.5446173548698425, 0.640938937664032, 0.6792607307434082, 0.5080864429473877, 0.3792526125907898]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7385262250900269})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6224019527435303})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6749382019042969})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6942485570907593})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6692732572555542})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.5576205078125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8076856136322021})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5813231468200684})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.571379542350769})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5523951053619385})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 57599], ['id', 39355], ['id', 18130], ['id', 11648], ['id', 34508], ['id', 55591], ['id', 45728], ['id', 48638], ['id', 34496], ['id', 49739]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3092760443687439, 0.3516571521759033, 0.4010202884674072, 0.5585167407989502, 0.6545519828796387, 0.4906761646270752, 0.6541316509246826, 0.4599947929382324, 0.20464164018630981, 0.5066027641296387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8338199853897095})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6994187831878662})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6711835265159607})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7262709736824036})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7205900549888611})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7250508069992065})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9036, 'crossentropy': 0.584637646484375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6697337627410889})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5588868856430054})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5003063678741455})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.4879130721092224})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.463553249835968})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 26418], ['id', 45024], ['id', 47511], ['id', 23137], ['id', 49146], ['id', 25116], ['id', 7811], ['id', 30041], ['id', 3136], ['id', 22555]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4766416549682617, 0.30450302362442017, 0.408075213432312, 0.5757134556770325, 0.30450695753097534, 0.3802480697631836, 0.2911590337753296, 0.3420976400375366, 0.4207005500793457, 0.42614567279815674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7809444665908813})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5696325898170471})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5900939106941223})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5487345457077026})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6973187923431396})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6188273429870605})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6608939170837402})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.50385078125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7469324469566345})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5021654367446899})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4601300358772278})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.44519931077957153})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4243203103542328})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.42303135991096497})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 35482], ['id', 17684], ['id', 5394], ['id', 14070], ['id', 36760], ['id', 22597], ['id', 52392], ['id', 41487], ['id', 25281], ['id', 52624]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.534361720085144, 0.3115200996398926, 0.5139307379722595, 0.5110586881637573, 0.5047740936279297, 0.457114040851593, 0.5568910837173462, 0.4156993627548218, 0.31362444162368774, 0.395907461643219]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7310911417007446})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5740509033203125})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5479933023452759})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5548325777053833})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6157386898994446})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6795976161956787})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.46801767578125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7048746347427368})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.49164292216300964})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4499472975730896})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.421714723110199})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4194929003715515})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 6304], ['id', 37996], ['id', 14655], ['id', 29259], ['id', 26600], ['id', 56076], ['id', 20641], ['id', 1285], ['id', 7924], ['id', 4797]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4986022114753723, 0.4867449998855591, 0.5141300559043884, 0.4844593405723572, 0.36583131551742554, 0.44047224521636963, 0.6614739894866943, 0.29757028818130493, 0.452275812625885, 0.48740971088409424]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0210869312286377})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6189310550689697})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5727921724319458})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5024667978286743})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5427524447441101})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.563705325126648})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5879493355751038})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.424939599609375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7382718324661255})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5096728801727295})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.45350223779678345})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43703269958496094})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.42348724603652954})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3939012587070465})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 54002], ['id', 22522], ['id', 42799], ['id', 33954], ['id', 18468], ['id', 16916], ['id', 19522], ['id', 48546], ['id', 24828], ['id', 43364]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4820050597190857, 0.5780704021453857, 0.27825450897216797, 0.3254615068435669, 0.5324039459228516, 0.43187862634658813, 0.47433534264564514, 0.48952221870422363, 0.33914774656295776, 0.4937436580657959]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8972296714782715})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5212308168411255})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5612631440162659})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5309284925460815})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5473566651344299})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9347, 'crossentropy': 0.46993349609375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7186634540557861})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5379409193992615})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5071786046028137})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47283685207366943})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 20892], ['id', 15188], ['id', 17011], ['id', 15289], ['id', 37315], ['id', 59303], ['id', 27316], ['id', 26452], ['id', 28231], ['id', 59711]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.42369502782821655, 0.49946945905685425, 0.39028918743133545, 0.2650715112686157, 0.4102116823196411, 0.47489237785339355, 0.4226810932159424, 0.3992753028869629, 0.31521397829055786, 0.27322685718536377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.796451210975647})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5089392066001892})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4925907254219055})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.488163024187088})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4721153974533081})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4916097819805145})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49278587102890015})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.511854887008667})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9469, 'crossentropy': 0.40581796875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6371774673461914})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43588048219680786})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4312713146209717})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3866274654865265})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3483833074569702})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3552703857421875})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3714348077774048})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 45088], ['id', 49890], ['id', 20068], ['id', 49016], ['id', 34716], ['id', 34737], ['id', 9180], ['id', 22083], ['id', 20862], ['ood', 44164]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4212850332260132, 0.7655799984931946, 0.590798020362854, 0.5634157061576843, 0.41416335105895996, 0.5450385510921478, 0.5024822950363159, 0.6124858856201172, 0.46032238006591797, 0.3130927085876465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8896822929382324})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5209403038024902})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5012956261634827})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4773175120353699})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48114240169525146})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4808052182197571})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5000194311141968})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9421, 'crossentropy': 0.41798798828125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6767996549606323})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4857311248779297})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3910020589828491})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4013715386390686})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.3810526728630066})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3780004382133484})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 23028], ['id', 34406], ['id', 28719], ['id', 52923], ['id', 9244], ['id', 9966], ['id', 39822], ['id', 12876], ['id', 45282], ['id', 29472]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5134975910186768, 0.5614618062973022, 0.48579490184783936, 0.5224059820175171, 0.2758252024650574, 0.5736790895462036, 0.3346618413925171, 0.46758484840393066, 0.300371915102005, 0.5039057731628418]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8405990600585938})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4583393633365631})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4302259683609009})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.44123026728630066})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43960970640182495})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4308338463306427})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9496, 'crossentropy': 0.350056201171875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6936895847320557})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4747893810272217})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.41815248131752014})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4107590615749359})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4116813540458679})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 52747], ['id', 6894], ['id', 32276], ['id', 40708], ['id', 33340], ['ood', 11622], ['id', 2352], ['id', 48278], ['id', 36452], ['id', 41590]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4620293378829956, 0.43391668796539307, 0.4682130217552185, 0.3836177587509155, 0.4135737419128418, 0.19463634490966797, 0.3662514090538025, 0.3647361993789673, 0.38185596466064453, 0.29643988609313965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8244478702545166})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47086000442504883})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.44298577308654785})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39472049474716187})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38047200441360474})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3614567816257477})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4179961085319519})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40020230412483215})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4337213635444641})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9529, 'crossentropy': 0.3270843994140625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7024096846580505})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44749462604522705})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.38449999690055847})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3611751198768616})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34158772230148315})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32224392890930176})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.30860280990600586})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.32279670238494873})
store['active_learning_steps'][17]['eval_training']['best_epoch']=7
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 49466], ['ood', 6487], ['id', 45917], ['id', 39421], ['id', 15855], ['id', 35480], ['id', 44827], ['id', 17486], ['id', 54646], ['ood', 7392]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.2976307272911072, 0.3989471197128296, 0.6353058218955994, 0.5949206352233887, 0.49921363592147827, 0.3911663889884949, 0.4626595377922058, 0.38581764698028564, 0.5380303859710693, 0.21644622087478638]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9053215980529785})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5058261156082153})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.41999804973602295})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4473741054534912})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.46097657084465027})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.455660879611969})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9475, 'crossentropy': 0.3640167724609375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7282799482345581})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.44669127464294434})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3975892663002014})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3829561471939087})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4029451012611389})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 28182], ['id', 22808], ['id', 32678], ['ood', 44581], ['id', 13243], ['id', 55190], ['id', 13259], ['id', 57116], ['id', 14845], ['id', 24263]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4791611433029175, 0.19304466247558594, 0.22042888402938843, 0.22095656394958496, 0.18970632553100586, 0.38545477390289307, 0.4977051019668579, 0.2547428607940674, 0.43489134311676025, 0.36185401678085327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.988325834274292})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5088965892791748})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4672344923019409})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40932345390319824})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4387305676937103})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43839550018310547})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45439979434013367})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9499, 'crossentropy': 0.3564472412109375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7588558197021484})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5306389331817627})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.45110100507736206})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.41402316093444824})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.41596662998199463})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37298864126205444})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 11227], ['id', 2856], ['id', 57507], ['id', 13109], ['ood', 12897], ['id', 45944], ['id', 47513], ['id', 13186], ['id', 2580], ['id', 38940]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.31735479831695557, 0.5692130327224731, 0.5801976323127747, 0.4336585998535156, 0.24142611026763916, 0.4719027876853943, 0.44367802143096924, 0.3535633087158203, 0.4463098645210266, 0.23966991901397705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9788215160369873})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5249496698379517})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44533705711364746})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3942142128944397})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4025402069091797})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38604098558425903})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4060608148574829})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4121335744857788})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42548519372940063})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9563, 'crossentropy': 0.3220330078125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6886974573135376})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.475003182888031})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3987804353237152})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35009509325027466})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3691233694553375})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.33385229110717773})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33890748023986816})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34468722343444824})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 38920], ['id', 10736], ['id', 59314], ['id', 32519], ['id', 48384], ['id', 35694], ['id', 34677], ['id', 10844], ['id', 58653], ['id', 22648]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.46871089935302734, 0.34766054153442383, 0.3020215630531311, 0.3777681589126587, 0.601732611656189, 0.4941481351852417, 0.45372748374938965, 0.44031819701194763, 0.30813050270080566, 0.488813579082489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9544650316238403})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5603047013282776})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40088415145874023})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41772162914276123})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4269651174545288})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3845127820968628})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44914960861206055})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42211592197418213})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4291270673274994})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9573, 'crossentropy': 0.31676005859375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7325736284255981})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45942240953445435})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.38211965560913086})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37255996465682983})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3838781714439392})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.32643288373947144})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3223711848258972})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3114091157913208})
store['active_learning_steps'][21]['eval_training']['best_epoch']=8
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 42122], ['id', 31988], ['id', 15185], ['id', 4160], ['id', 36065], ['id', 19814], ['id', 57004], ['id', 9448], ['id', 50905], ['id', 39419]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.43070361018180847, 0.6127434372901917, 0.6225627660751343, 0.37672215700149536, 0.623699963092804, 0.4141262173652649, 0.31050390005111694, 0.34972310066223145, 0.47456181049346924, 0.4710233807563782]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9265152215957642})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46921706199645996})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37697234749794006})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32213813066482544})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.336142897605896})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3268224596977234})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35541200637817383})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9602, 'crossentropy': 0.302296142578125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7775305509567261})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4668278694152832})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.410800576210022})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34218743443489075})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3531389832496643})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3143497407436371})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 31148], ['id', 45770], ['id', 43372], ['id', 33572], ['id', 20206], ['id', 6418], ['id', 6197], ['id', 30900], ['id', 18446], ['id', 1024]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5555897951126099, 0.46761757135391235, 0.33976221084594727, 0.3926510810852051, 0.4979246258735657, 0.4145512580871582, 0.3660455346107483, 0.5711753368377686, 0.3498089909553528, 0.5270727872848511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9187110662460327})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5975103378295898})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3919643759727478})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35643208026885986})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.37044617533683777})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3629801869392395})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3449968993663788})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33113592863082886})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36354660987854004})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3846471309661865})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4175451099872589})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9621, 'crossentropy': 0.292077783203125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7949849963188171})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.516019344329834})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38617151975631714})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35028550028800964})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3244314193725586})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.31472939252853394})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3254212737083435})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.27625131607055664})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.27169686555862427})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.27301308512687683})
store['active_learning_steps'][23]['eval_training']['best_epoch']=9
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 3730], ['id', 48767], ['id', 39516], ['id', 2761], ['id', 30862], ['id', 26338], ['id', 12089], ['id', 53196], ['id', 42774], ['id', 42703]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.37265896797180176, 0.3938027620315552, 0.5330637097358704, 0.5840228199958801, 0.32673102617263794, 0.5135136246681213, 0.462075799703598, 0.36559516191482544, 0.40092939138412476, 0.6400501132011414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0245085954666138})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4527103304862976})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4076182246208191})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32649821043014526})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3240230977535248})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34550708532333374})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30103743076324463})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3387686014175415})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33210617303848267})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34334516525268555})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9623, 'crossentropy': 0.272849951171875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.791332483291626})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43867191672325134})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37343794107437134})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3171461820602417})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2816709876060486})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3093225359916687})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3053629994392395})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2786073386669159})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2729329466819763})
store['active_learning_steps'][24]['eval_training']['best_epoch']=9
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 46126], ['id', 47140], ['id', 33162], ['id', 50393], ['id', 55015], ['id', 20037], ['id', 29827], ['id', 57665], ['id', 2184], ['id', 56288]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2741585373878479, 0.39023900032043457, 0.5897477865219116, 0.38633108139038086, 0.3661813735961914, 0.4139939546585083, 0.39414316415786743, 0.46102774143218994, 0.4171733260154724, 0.34282803535461426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.025870680809021})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5672610402107239})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37302806973457336})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.35445764660835266})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3369365930557251})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3802573084831238})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33533331751823425})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3487202525138855})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29986876249313354})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35658377408981323})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3399360477924347})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38147497177124023})
store['active_learning_steps'][25]['training']['best_epoch']=9
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.294458642578125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7764787077903748})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41493964195251465})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3373517394065857})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.324074387550354})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2880769968032837})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28681740164756775})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2525019645690918})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25524693727493286})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2655590772628784})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2456667721271515})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22986753284931183})
store['active_learning_steps'][25]['eval_training']['best_epoch']=11
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 37779], ['id', 59808], ['id', 32499], ['id', 55496], ['id', 23086], ['id', 35105], ['id', 7233], ['id', 58660], ['id', 25998], ['id', 42434]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5642140209674835, 0.480170875787735, 0.2816484570503235, 0.7324036359786987, 0.5275827646255493, 0.5071427226066589, 0.5337894558906555, 0.576551079750061, 0.46483272314071655, 0.6035154163837433]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9949520826339722})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5198013186454773})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3972721993923187})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35645127296447754})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3244486451148987})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2967333197593689})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3533874750137329})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3234551250934601})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.307567298412323})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.2756423095703125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8172755241394043})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.517831563949585})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40099358558654785})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33105963468551636})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.327085018157959})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32624492049217224})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28375861048698425})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27600085735321045})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 13538], ['id', 1674], ['id', 45490], ['id', 44972], ['ood', 49044], ['id', 36268], ['ood', 30924], ['id', 41334], ['ood', 38401], ['ood', 6735]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.45071035623550415, 0.5598626732826233, 0.31627368927001953, 0.3372197151184082, 0.22494006156921387, 0.40052029490470886, 0.3048064708709717, 0.37334996461868286, 0.2264035940170288, 0.1847841739654541]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.004475712776184})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4728182554244995})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.382889986038208})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33924609422683716})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3517269790172577})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3349040150642395})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33382952213287354})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34976911544799805})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3589962124824524})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32472050189971924})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3430902361869812})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3361464738845825})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3581918776035309})
store['active_learning_steps'][27]['training']['best_epoch']=10
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.296743212890625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.83014976978302})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46674269437789917})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3700100779533386})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3415752053260803})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27181893587112427})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28039848804473877})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2649311423301697})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28144633769989014})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.25223156809806824})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.24278302490711212})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25052523612976074})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24840877950191498})
store['active_learning_steps'][27]['eval_training']['best_epoch']=10
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 22130], ['id', 33224], ['id', 6929], ['id', 13234], ['id', 19866], ['id', 40494], ['id', 53015], ['id', 22034], ['id', 3798], ['id', 44496]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3912379741668701, 0.38464558124542236, 0.45609477162361145, 0.7430485188961029, 0.49166789650917053, 0.4675077199935913, 0.33628982305526733, 0.4583553671836853, 0.5981423258781433, 0.4803067147731781]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.127126693725586})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5132668614387512})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3674713969230652})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35019659996032715})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35791105031967163})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31569528579711914})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.331149697303772})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3551902174949646})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3465269207954407})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9638, 'crossentropy': 0.2846737060546875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8280774354934692})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5094558000564575})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3729839324951172})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34180891513824463})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33334100246429443})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3068138659000397})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30566057562828064})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2905709743499756})
store['active_learning_steps'][28]['eval_training']['best_epoch']=8
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 38791], ['id', 49487], ['ood', 42381], ['id', 13524], ['id', 30884], ['id', 34328], ['id', 14706], ['id', 30016], ['id', 19159], ['id', 32372]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4009832739830017, 0.42267298698425293, 0.3052469491958618, 0.5140156745910645, 0.43265610933303833, 0.5390061140060425, 0.43718844652175903, 0.3114597797393799, 0.38223475217819214, 0.5108752846717834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0116856098175049})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.549127459526062})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3672366738319397})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3534184694290161})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33445996046066284})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3035511076450348})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.304443359375})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30378687381744385})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31739646196365356})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9621, 'crossentropy': 0.286703369140625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9384218454360962})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5341035723686218})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38167107105255127})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3359520733356476})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32652992010116577})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3332802653312683})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31012946367263794})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31895285844802856})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 17540], ['id', 8116], ['id', 49744], ['id', 36363], ['id', 40702], ['id', 56066], ['id', 21058], ['id', 6050], ['id', 36818], ['id', 41352]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4780240058898926, 0.47946077585220337, 0.41364574432373047, 0.5250418782234192, 0.44880837202072144, 0.4100543260574341, 0.523047685623169, 0.3955777883529663, 0.41848671436309814, 0.380512535572052]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.150264859199524})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5976642370223999})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40536361932754517})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3558574318885803})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.328741192817688})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3302445411682129})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3109915554523468})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36372488737106323})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35433727502822876})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3549196720123291})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.2756167236328125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9683663249015808})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5304038524627686})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4532025158405304})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3505699634552002})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33599215745925903})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2980955243110657})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3050406575202942})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28800857067108154})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29177844524383545})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 59423], ['ood', 2139], ['ood', 28417], ['ood', 56104], ['id', 25516], ['id', 17697], ['ood', 45084], ['id', 26392], ['ood', 27863], ['ood', 23586]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.22352850437164307, 0.31513214111328125, 0.45232093334198, 0.4442012310028076, 0.4440349340438843, 0.5267255902290344, 0.41624653339385986, 0.32357290387153625, 0.45446276664733887, 0.21400976181030273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0314788818359375})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5397570133209229})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3966507911682129})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3517377972602844})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3282722234725952})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30824828147888184})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2809312343597412})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28421637415885925})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2861329913139343})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32863008975982666})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.26389970703125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9677610397338867})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5192291736602783})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38223445415496826})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33636826276779175})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3090723156929016})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30336374044418335})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30626726150512695})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28453803062438965})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24448345601558685})
store['active_learning_steps'][31]['eval_training']['best_epoch']=9
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 35643], ['id', 28536], ['id', 30429], ['id', 54556], ['id', 24462], ['id', 7612], ['id', 55505], ['id', 46658], ['id', 30658], ['id', 18031]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41750699281692505, 0.3935394883155823, 0.5648062229156494, 0.3509335517883301, 0.4502020478248596, 0.5128838419914246, 0.24863111972808838, 0.5046383738517761, 0.45306000113487244, 0.41913437843322754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.174702525138855})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5635215640068054})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45020735263824463})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3526191711425781})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3138030171394348})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32517164945602417})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3142414093017578})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3199559152126312})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9648, 'crossentropy': 0.29593798828125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9233410358428955})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48792874813079834})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44981223344802856})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39798086881637573})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3511263430118561})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3267633318901062})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34936732053756714})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 33042], ['id', 25386], ['id', 49084], ['ood', 16731], ['id', 28810], ['id', 41377], ['id', 38337], ['id', 25310], ['id', 18378], ['id', 43072]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4162999987602234, 0.3452972173690796, 0.34386497735977173, 0.3288853168487549, 0.3552892208099365, 0.260165810585022, 0.2624448537826538, 0.2512780427932739, 0.3408513069152832, 0.4215494394302368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0620684623718262})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5330833196640015})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40494227409362793})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3390611410140991})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.344596803188324})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31446415185928345})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29868143796920776})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3250162601470947})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3274027109146118})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34483224153518677})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.26522451171875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.843467116355896})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44236254692077637})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.36538225412368774})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.32474485039711})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32698673009872437})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2933429479598999})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28607356548309326})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2873920798301697})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2985566556453705})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 23463], ['id', 38605], ['id', 56380], ['id', 17121], ['id', 53999], ['id', 57773], ['id', 22062], ['id', 43950], ['id', 44013], ['id', 43745]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.425703227519989, 0.39242130517959595, 0.44467055797576904, 0.4345093369483948, 0.5178776383399963, 0.42990338802337646, 0.4548605680465698, 0.5164929032325745, 0.5516624450683594, 0.4952649474143982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1594302654266357})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6035540699958801})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3960074782371521})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33273327350616455})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2920183539390564})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30483049154281616})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3141756057739258})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2894667983055115})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3008844256401062})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30999553203582764})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32773762941360474})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9667, 'crossentropy': 0.2648511962890625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.936019778251648})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48487234115600586})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43334341049194336})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3624957203865051})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30805784463882446})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28981584310531616})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2876758277416229})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2618507742881775})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2843681275844574})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29614800214767456})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 26020], ['id', 16688], ['id', 39749], ['id', 1600], ['id', 59757], ['id', 52228], ['id', 49957], ['id', 37450], ['id', 12268], ['id', 49895]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4676682651042938, 0.33816421031951904, 0.4274042248725891, 0.514376699924469, 0.470775842666626, 0.5719613432884216, 0.6703185439109802, 0.5562188625335693, 0.2736465632915497, 0.5686022639274597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.129223346710205})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5137103199958801})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4239901900291443})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3249679207801819})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36276721954345703})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29677829146385193})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32719945907592773})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28970545530319214})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30891311168670654})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33214855194091797})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3504587411880493})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.27187197265625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.9543329477310181})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5071579813957214})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37409278750419617})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3601170778274536})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3295630216598511})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33572787046432495})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3300715684890747})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30311962962150574})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2879868149757385})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2692313492298126})
store['active_learning_steps'][35]['eval_training']['best_epoch']=10
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 2302], ['id', 16823], ['id', 40530], ['id', 41832], ['id', 52138], ['id', 20162], ['id', 46714], ['id', 33601], ['id', 8950], ['id', 36744]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.38528239727020264, 0.4187414050102234, 0.4371410012245178, 0.41412127017974854, 0.354328989982605, 0.5221139788627625, 0.4793190360069275, 0.3223806619644165, 0.24638661742210388, 0.3636183738708496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0118024349212646})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4424920678138733})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38157087564468384})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3428761959075928})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2752920389175415})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3025687038898468})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25194674730300903})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.268723726272583})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2896862030029297})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26702845096588135})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.224088134765625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8213417530059814})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.49816203117370605})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37052708864212036})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3249417543411255})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29185399413108826})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3136366009712219})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24772246181964874})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2715729773044586})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2601296603679657})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 41426], ['id', 27172], ['id', 132], ['id', 37591], ['id', 14305], ['id', 17507], ['id', 26412], ['id', 58560], ['id', 4663], ['id', 56108]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40350669622421265, 0.4070340394973755, 0.34392112493515015, 0.3640638589859009, 0.36583447456359863, 0.3220522403717041, 0.3911014795303345, 0.4661523103713989, 0.29668599367141724, 0.4009777307510376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1832027435302734})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6739122867584229})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44428756833076477})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3309209942817688})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29260164499282837})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3108372092247009})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2766135632991791})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3021979033946991})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31101903319358826})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28231334686279297})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.2402888671875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8591536283493042})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4643886387348175})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39855068922042847})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32322123646736145})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3160639703273773})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29568928480148315})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2902027368545532})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28204888105392456})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2846946120262146})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 12522], ['id', 46673], ['id', 35232], ['id', 34660], ['id', 8853], ['id', 22759], ['id', 3118], ['id', 44466], ['id', 6399], ['id', 14385]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4177704453468323, 0.26788604259490967, 0.6014877259731293, 0.41961824893951416, 0.4046977758407593, 0.33773213624954224, 0.29862481355667114, 0.3576141595840454, 0.3408101499080658, 0.4647555947303772]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.1749945878982544})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5291571617126465})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3366332948207855})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30116981267929077})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28248971700668335})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27224665880203247})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2851306200027466})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28835320472717285})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2692015469074249})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2850649058818817})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2938530743122101})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2563885748386383})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2909281253814697})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2874118685722351})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32735776901245117})
store['active_learning_steps'][38]['training']['best_epoch']=12
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9749, 'crossentropy': 0.225905126953125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0052447319030762})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5600490570068359})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38448500633239746})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3662889003753662})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28167396783828735})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2799910306930542})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2541484832763672})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24109327793121338})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24255016446113586})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24848227202892303})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24248617887496948})
store['active_learning_steps'][38]['eval_training']['best_epoch']=8
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 26426], ['id', 14762], ['id', 45437], ['id', 54880], ['id', 47291], ['id', 32065], ['id', 32453], ['id', 14002], ['id', 49041], ['id', 2765]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39008206129074097, 0.37107494473457336, 0.3854138255119324, 0.4751065969467163, 0.32810449600219727, 0.20598313212394714, 0.3758500814437866, 0.2932782769203186, 0.35321903228759766, 0.4754735231399536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2195799350738525})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6049100160598755})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41239726543426514})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.33388611674308777})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35251492261886597})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3217768371105194})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27650463581085205})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3047843277454376})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29594600200653076})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29660362005233765})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.271452294921875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9003450870513916})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5329982042312622})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4126836061477661})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3643977642059326})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3351348340511322})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29413387179374695})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.289816677570343})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28052929043769836})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28651854395866394})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 54582], ['id', 21436], ['id', 53156], ['id', 32018], ['id', 55906], ['id', 32343], ['ood', 3118], ['id', 34968], ['id', 6044], ['id', 991]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.28857630491256714, 0.5347357392311096, 0.4383617043495178, 0.4034996032714844, 0.5023853778839111, 0.40155738592147827, 0.22256755828857422, 0.332835853099823, 0.5136759281158447, 0.41199612617492676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.16480553150177})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5796425342559814})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39483192563056946})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33816492557525635})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30638402700424194})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29383543133735657})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2815992832183838})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25085926055908203})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2824484705924988})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26215383410453796})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27599090337753296})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9737, 'crossentropy': 0.2327349853515625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8884465098381042})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4032033681869507})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3511567711830139})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33321499824523926})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3025333881378174})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25524118542671204})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26981550455093384})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2516721487045288})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2205921709537506})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23935747146606445})
store['active_learning_steps'][40]['eval_training']['best_epoch']=9
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 54759], ['ood', 55163], ['id', 10028], ['id', 9490], ['id', 39561], ['id', 5265], ['id', 5035], ['id', 22200], ['id', 17700], ['id', 38389]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.32122188806533813, 0.2131037712097168, 0.4684670567512512, 0.44864606857299805, 0.36135366559028625, 0.361799955368042, 0.4383409023284912, 0.38136476278305054, 0.4698448181152344, 0.4544405937194824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1619127988815308})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.5428184270858765})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36082208156585693})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32013076543807983})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28856849670410156})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2737080156803131})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2749803066253662})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2739619016647339})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24901220202445984})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27166658639907837})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24689409136772156})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26976579427719116})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26444318890571594})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27625176310539246})
store['active_learning_steps'][41]['training']['best_epoch']=11
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9745, 'crossentropy': 0.230877490234375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9857667684555054})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5007249712944031})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4410405457019806})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3384399712085724})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3011576235294342})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2614023983478546})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28229305148124695})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26612797379493713})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2560499310493469})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25340965390205383})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25183171033859253})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25778380036354065})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23544183373451233})
store['active_learning_steps'][41]['eval_training']['best_epoch']=13
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 11767], ['id', 47600], ['id', 50331], ['id', 50445], ['id', 41218], ['id', 37469], ['id', 24646], ['id', 8200], ['id', 31301], ['ood', 9117]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5647826790809631, 0.5250316262245178, 0.44867604970932007, 0.5804498195648193, 0.44322842359542847, 0.5240570306777954, 0.3562191128730774, 0.585055947303772, 0.4494706988334656, 0.3164917230606079]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.17945396900177})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5743733048439026})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3968929648399353})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3297703266143799})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2801162004470825})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9814453125, 'crossentropy': 0.2613922953605652})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26866263151168823})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24903279542922974})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26693183183670044})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.24760866165161133})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2637633979320526})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24568676948547363})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.27642661333084106})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.26553964614868164})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27460533380508423})
store['active_learning_steps'][42]['training']['best_epoch']=12
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9761, 'crossentropy': 0.225729638671875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.997921347618103})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5499999523162842})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34516483545303345})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33779579401016235})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27797049283981323})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27082204818725586})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28723394870758057})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2448454350233078})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24402107298374176})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25664642453193665})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2516535222530365})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.23587441444396973})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23353269696235657})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2579265832901001})
store['active_learning_steps'][42]['eval_training']['best_epoch']=13
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 13998], ['id', 12651], ['id', 36141], ['id', 6604], ['id', 55368], ['id', 37704], ['id', 56292], ['id', 23567], ['id', 8865], ['id', 36408]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5981928706169128, 0.4387403130531311, 0.6302308440208435, 0.5878903269767761, 0.6008807420730591, 0.3387988209724426, 0.521783709526062, 0.4213929772377014, 0.4657360315322876, 0.549798846244812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.310905933380127})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7875769734382629})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.5307744145393372})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39261263608932495})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3515843152999878})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30616939067840576})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27933090925216675})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2932371497154236})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2814441919326782})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2658616304397583})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2677220106124878})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29909080266952515})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.3107297122478485})
store['active_learning_steps'][43]['training']['best_epoch']=10
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.2659632080078125}
